-- Tracing Finland's Innovation State — v0.1 schema (PostgreSQL 15+ with pgvector)
-- Run: psql -d innovation_state -f db/schema.sql

CREATE EXTENSION IF NOT EXISTS vector;

-- 1. Sources --------------------------------------------------------------
CREATE TABLE document (
    id            TEXT PRIMARY KEY,           -- e.g. GP64, RC1990 (matches corpus CSV)
    series        TEXT NOT NULL,              -- government_programme | council_review | anchor | external | startup
    title         TEXT NOT NULL,
    publisher     TEXT,
    date          DATE,
    date_end      DATE,
    language      TEXT DEFAULT 'fi',
    url           TEXT,
    source_quality TEXT,                      -- html | pdf_text | pdf_ocr
    text          TEXT,
    fetched_at    TIMESTAMPTZ DEFAULT now()
);

-- Chunks for semantic search; page/char offsets keep evidence citable
CREATE TABLE chunk (
    id            BIGSERIAL PRIMARY KEY,
    document_id   TEXT REFERENCES document(id) ON DELETE CASCADE,
    seq           INT NOT NULL,
    page          INT,
    char_start    INT,
    char_end      INT,
    text          TEXT NOT NULL,
    embedding     vector(1024)                -- match your embedding model's dimension
);
CREATE INDEX ON chunk USING hnsw (embedding vector_cosine_ops);

-- 2. Vocabulary tracker ---------------------------------------------------
CREATE TABLE concept (
    id            TEXT PRIMARY KEY,           -- e.g. national_innovation_system
    label_en      TEXT NOT NULL,
    label_fi      TEXT,
    description   TEXT
);

CREATE TABLE concept_variant (               -- surface forms incl. Finnish inflections
    concept_id    TEXT REFERENCES concept(id),
    variant       TEXT NOT NULL,
    language      TEXT NOT NULL,
    PRIMARY KEY (concept_id, variant)
);

CREATE TABLE concept_mention (
    document_id   TEXT REFERENCES document(id) ON DELETE CASCADE,
    concept_id    TEXT REFERENCES concept(id),
    count         INT NOT NULL,
    per_10k_words NUMERIC,                    -- normalised: documents differ hugely in length
    method        TEXT,                       -- lexical | llm
    PRIMARY KEY (document_id, concept_id, method)
);

-- 3. Claims and evidence (the core) ---------------------------------------
-- layer: evidence = what a document says; relation = extracted link; interpretation = our reading
CREATE TABLE claim (
    id            BIGSERIAL PRIMARY KEY,
    text          TEXT NOT NULL,
    layer         TEXT NOT NULL CHECK (layer IN ('evidence','relation','interpretation')),
    claim_type    TEXT,                       -- problem | policy_idea | instrument | goal | outcome | assessment
    date_from     DATE,
    date_to       DATE,
    confidence    NUMERIC CHECK (confidence BETWEEN 0 AND 1),
    created_by    TEXT,                       -- model name + prompt version, or 'human'
    reviewed      BOOLEAN DEFAULT false,
    created_at    TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE claim_source (
    claim_id      BIGINT REFERENCES claim(id) ON DELETE CASCADE,
    document_id   TEXT REFERENCES document(id),
    chunk_id      BIGINT REFERENCES chunk(id),
    page          INT,
    excerpt       TEXT NOT NULL,              -- exact passage, original language
    stance        TEXT DEFAULT 'supports' CHECK (stance IN ('supports','contradicts','qualifies')),
    PRIMARY KEY (claim_id, document_id, excerpt)
);

-- An interpretation rests on evidence claims
CREATE TABLE claim_basis (
    claim_id      BIGINT REFERENCES claim(id) ON DELETE CASCADE,
    basis_claim_id BIGINT REFERENCES claim(id),
    PRIMARY KEY (claim_id, basis_claim_id)
);

-- 4. Entities and relations (graph-in-tables; no graph DB in v0.1) --------
-- Institutions, programmes, policies, companies. No profiling of named individuals.
CREATE TABLE entity (
    id            TEXT PRIMARY KEY,           -- e.g. tekes, business_finland, shok
    name          TEXT NOT NULL,
    kind          TEXT NOT NULL,              -- ministry | agency | council | university | research_institute | programme | policy | company | event
    start_date    DATE,
    end_date      DATE,
    description   TEXT
);

CREATE TABLE relationship (
    id            BIGSERIAL PRIMARY KEY,
    source_id     TEXT REFERENCES entity(id),
    type          TEXT NOT NULL,              -- funded | created | merged_into | evaluated | replaced | coordinated
    target_id     TEXT REFERENCES entity(id),
    start_date    DATE,
    end_date      DATE,
    claim_id      BIGINT REFERENCES claim(id) -- every edge traces back to a claim and its evidence
);

CREATE TABLE claim_entity (
    claim_id      BIGINT REFERENCES claim(id) ON DELETE CASCADE,
    entity_id     TEXT REFERENCES entity(id),
    role          TEXT,                       -- actor | target | instrument_owner
    PRIMARY KEY (claim_id, entity_id)
);
