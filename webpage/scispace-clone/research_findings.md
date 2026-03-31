# SciSpace.com Tech Stack & Architecture Research

> **Note**: SciSpace.com blocks automated access with Cloudflare human verification. Direct tech stack analysis was not possible. Information below is compiled from job postings, company pages, and analysis of similar platforms.

---

## 1. SciSpace Company Overview

### Basic Information
- **Former Name**: Typeset.io
- **Headquarters**: Bangalore, India (HSR Layout, Sector 6) + San Francisco, California
- **Founded**: As Typeset.io
- **Domain**: SaaS, Academia, Research, Scientific Research, Authoring Platform, Literature Review, Copilot for Researchers
- **Funding**: Backed by investors (Crunchbase data accessible)

### Core Product Features
- AI-powered research paper search and discovery
- Paper explanation and summarization
- Literature review automation
- Citation finding and management
- Research workflow assistance
- Interactive reading experience

---

## 2. Direct Tech Stack Findings (Limited)

Due to Cloudflare blocking, direct W3Techs/BuiltWith analysis was not possible. Based on LinkedIn job postings, the following roles are advertised:

### Observed Job Postings
- Senior Gen AI Engineer (Bangalore)
- User Experience Designer
- Director of Data Science
- Product Designer
- Machine Learning Engineer
- Research And Development Engineer

---

## 3. Similar Academic/Research AI Platforms (Detailed Architecture Analysis)

Since direct SciSpace analysis was blocked, the following **architecturally similar platforms** provide excellent reference implementations:

### 3.1 Elicit (elicit.org)

**Overview**: AI-powered research assistant trusted by 5M+ researchers, including those at top pharmaceutical companies.

#### Tech Stack (Inferred from Engineering Blog)
- **Frontend**: React (inferred from modern SPA patterns, "living documents" in browser)
- **Backend**: Python-based ML infrastructure
- **AI/ML**: Claude Opus 4.5 (Anthropic), GPT models (OpenAI), custom SPLADE models
- **Search**: Hybrid approach combining:
  - SPLADE (Sparse Lexical and Expansion) for transparent, reproducible search
  - Semantic embeddings (via OpenAI/Custom)
  - BM25/keyword search
  - Re-ranking with LLM
- **Data Pipeline**:
  - 138M+ academic papers indexed
  - 545,000 clinical trials (ClinicalTrials.gov integration)
  - Semantic Scholar as data source
- **API**: REST API with JSON responses, async report generation

#### Key Architecture Blog Insights

**Search Architecture** (from "Build a Search Engine, Not a Vector DB"):
```
1. Embeddings + Traditional Search Combined
   - Vector similarity search (dense)
   - BM25 keyword search
   - Hybrid blending

2. Query Expansion with LLMs
   - SPLADE: LLM suggests related terms
   - Deterministic and transparent
   - Reproducible results

3. Re-ranking
   - LLM-based relevancy scoring
   - Beat purpose-built systems
```

**Living Documents UX Pattern**:
```
- Browser-based editable table (papers x extractions)
- Frontend: Complex React SPA
- Backend: Job queue for 1000s of LLM calls
- Streaming updates to browser
- Cost tracking per action
- Credits-based billing system
```

**Research Agent Architecture** (Agentic workflows):
```
1. User prompt → Clarifying questions
2. Agent decomposes into systematic program
3. Multi-source search (publications, web, clinical trials)
4. Evidence synthesis
5. Iterative refinement via chat
```

**Data Sources Integrations**:
- PubMed
- ClinicalTrials.gov
- Semantic Scholar corpus
- Custom PDF uploads

#### API Architecture
```json
// Search endpoint (sync)
POST /search
{
  "query": "GLP-1 receptor agonists cardiovascular outcomes",
  "filter": {"year": 2020}
}
// Response: JSON with titles, authors, abstracts, citation counts, DOIs, PDF links

// Report generation (async)
POST /reports
{
  "query": "melatonin supplementation sleep quality",
  "maxPapers": 80
}
// Response: reportId → poll for completion (5-15 min)
```

---

### 3.2 Semantic Scholar (semanticscholar.org)

**Overview**: AI-powered academic search from Allen Institute for AI (AI2). Provides free API.

#### Tech Stack
- **Backend**: Python, Elasticsearch (implied by their CORPUS project)
- **Search**: Custom ML models (SPECTER2 embeddings)
- **Data**: Academic Graph with 200M+ papers
- **API**: REST, rate-limited (1000 req/s public, authenticated higher)

#### API Endpoints
```
GET /paper/{paperId}     - Paper metadata
GET /author/{authorId}   - Author information
GET /citation/{paperId}   - Citation network
GET /recommendations     - Similar paper recommendations
GET /datasets            - Bulk data downloads
```

#### Key Features
- SPECTER2: Paper embedding model (available via API)
- Citation graph analysis
- TLDR summarization
- PDF link extraction

---

### 3.3 Consensus (consensus.app)

**Overview**: AI-powered academic search engine focused on consensus extraction from papers.

#### Characteristics (from crawl)
- Search across academic papers
- Extract consensus positions from research
- AI chat interface
- Chrome extension available

---

### 3.4 Crossref / OpenAlex

**Overview**: Metadata infrastructure for academic research.

#### OpenAlex API
```
GET /works              - Search papers
GET /authors           - Author search
GET /institutions      - Institution data
GET /concepts          - Topic taxonomy
```

#### Architecture Pattern
- Linked Data / Knowledge Graph
- RESTful JSON API
- Webhooks for updates
- Bulk download options

---

## 4. Recommended Tech Stack for SciSpace Clone

Based on analysis of Elicit and similar platforms, here's a recommended architecture:

### 4.1 Frontend Stack
```
Framework:      Next.js 14+ (React) or Remix
UI Library:     shadcn/ui + Tailwind CSS or Radix UI
State:          Zustand or React Query (for server state)
Tables:         TanStack Table (virtualized for large datasets)
PDF Viewer:     PDF.js or react-pdf
Search UI:      Custom autocomplete + filters
Auth:           NextAuth.js / Clerk
```

### 4.2 Backend Stack
```
Runtime:        Node.js / Deno or Python (FastAPI)
Framework:      Next.js API routes OR Express/NestJS
ORM:            Prisma or Drizzle
Database:       PostgreSQL (Supabase / Neon)
Search Engine:  Elasticsearch / Typesense / Meilisearch
  - Hybrid: keyword + vector (SPLADE approach)
Cache:          Redis (Upstash)
Queue:          Inngest or BullMQ (for async jobs)
```

### 4.3 AI/ML Infrastructure
```
LLM Provider:   OpenAI API + Anthropic Claude API
Embeddings:    OpenAI text-embedding-3 OR Custom SPECTER2
Vector Store:  Pinecone / Qdrant / ChromaDB (for hybrid search)
Fine-tuning:   Possible for domain-specific models
RAG:           Build search-first, then augment (see Elicit blog)
```

### 4.4 Data Pipeline
```
Paper Ingestion:
  - Semantic Scholar API (free, 200M+ papers)
  - Crossref API (metadata)
  - arXiv API (preprints)
  - PubMed API (biomedical)

Processing:
  - PDF extraction (pdfparse / Grobid)
  - Text chunking for embeddings
  - Citation graph extraction

Storage:
  - PostgreSQL (metadata, user data)
  - S3/R2 (PDF storage)
  - Elasticsearch (full-text search)
  - Vector DB (embeddings)
```

### 4.5 Key Architectural Patterns from Elicit

**1. Search-First RAG**:
```
Don't: Embed everything, dump to vector DB, hope for best
Do: Build a proper search engine first (keyword + semantic)
     Then use LLM to re-rank and synthesize
```

**2. Living Documents Pattern**:
```
- Tables that grow in both X (papers) and Y (extractions)
- Streaming results to browser
- Job queue for 1000s of LLM calls
- Cost tracking per action
```

**3. Agentic Research Workflow**:
```
User Query → Clarifying Questions → Decompose into Tasks
→ Execute Search → Extract → Synthesize → Present
→ Iterate based on feedback
```

**4. Evaluation Infrastructure**:
```
- Evaluate search quality
- Track citation-level grounding
- Auto-evals for LLM accuracy
- Human feedback loops
```

---

## 5. Key Technical Differentiators

### Academic AI vs General AI

| Aspect | Academic AI | General AI |
|--------|-------------|------------|
| Search | Reproducible, auditable | Relevance only |
| Citations | Sentence-level grounding | Optional |
| Evaluation | Systematic reviews | User satisfaction |
| Scale | 1000s of papers per query | Few documents |
| Transparency | Explain ranking | Black-box |

### SPLADE vs Pure Vector Search

**SPLADE Advantages** (per Elicit blog):
1. Deterministic (same query = same results)
2. Transparent (can see expansion terms)
3. Reproducible (for systematic reviews)
4. Fast (uses BM25, not expensive ANN)
5. Domain-trainable (custom SPLADE models)

---

## 6. Open Source / Reference Implementations

### Relevant Open Source Projects
- **GROBID**: PDF extraction (Apache 2.0)
- **Elasticsearch**: Search engine
- **Meilisearch / Typesense**: Lightweight search alternatives
- **ChromaDB / Qdrant**: Vector databases
- **Haystack**: LLM framework (deepset)
- **LangChain**: LLM orchestration
- **CORPUS**: Allen AI's open academic graph

### Datasets
- **Semantic Scholar Academic Graph (S2AG)**: 200M+ papers, free
- **OpenAlex**: 240M+ works, CC-BY license
- **Crossref**: Metadata, DOI-based

---

## 7. Recommendations for Implementation

### Phase 1: Core Search
1. Set up Semantic Scholar API as data source
2. Implement hybrid search (keyword + semantic)
3. Build basic React frontend
4. Deploy with Vercel/Netlify

### Phase 2: AI Features
1. Add LLM summarization (OpenAI/Anthropic)
2. Implement citation extraction
3. Build "living document" table UI
4. Add async job queue

### Phase 3: Advanced
1. Fine-tune domain-specific models
2. Build agentic workflows
3. Add systematic review tools
4. Implement cost tracking/billing

---

## Sources

- Elicit Engineering Blog: https://blog.elicit.com
- Semantic Scholar API: https://api.semanticscholar.org
- OpenAlex API: https://openalex.org
- Crossref Documentation: https://www.crossref.org/documentation/
- LinkedIn Company Page: https://www.linkedin.com/company/scispace
- Elicit Homepage: https://elicit.org
- Semantic Scholar Homepage: https://www.semanticscholar.org
- Consensus: https://consensus.app

---

*Research compiled: 2026-03-31*
*Note: Direct tech stack analysis of scispace.com was blocked by Cloudflare verification. Findings based on similar platforms.*
