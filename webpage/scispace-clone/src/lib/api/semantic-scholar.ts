// Types for Semantic Scholar API
export interface Author {
  authorId: string;
  name: string;
  aliases?: string[];
  url?: string;
}

export interface Paper {
  paperId: string;
  title: string;
  authors: Author[];
  abstract: string | null;
  year: number | null;
  venue: string | null;
  citationCount: number;
  externalId: string | null;
  url?: string;
}

export interface SearchResult {
  total: number;
  offset: number;
  nextOffset: number | null;
  papers: Paper[];
}

export interface SearchFilters {
  query: string;
  yearFrom?: number;
  yearTo?: number;
  venue?: string;
  minCitations?: number;
  openAccessOnly?: boolean;
}

// Mock data for fallback
const MOCK_PAPERS: Paper[] = [
  {
    paperId: "1",
    title: "Attention Is All You Need",
    authors: [
      { authorId: "1", name: "Ashish Vaswani" },
      { authorId: "2", name: "Noam Shazeer" },
      { authorId: "3", name: "Niki Parmar" },
    ],
    abstract:
      "The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely.",
    year: 2017,
    venue: "NeurIPS",
    citationCount: 98000,
    externalId: "arXiv:1706.03762",
  },
  {
    paperId: "2",
    title: "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",
    authors: [
      { authorId: "4", name: "Jacob Devlin" },
      { authorId: "5", name: "Ming-Wei Chang" },
      { authorId: "6", name: "Kenton Lee" },
    ],
    abstract:
      "We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers. Unlike recent language representation models, BERT is designed to pre-train deep bidirectional representations from unlabeled text by jointly conditioning on both left and right context in all layers.",
    year: 2018,
    venue: "NAACL",
    citationCount: 85000,
    externalId: "arXiv:1810.04805",
  },
  {
    paperId: "3",
    title: "GPT-4 Technical Report",
    authors: [
      { authorId: "7", name: "OpenAI" },
    ],
    abstract:
      "We report the development of GPT-4, a large-scale, multimodal model which can accept image and text inputs and produce text outputs. GPT-4 exhibits human-level performance on various professional and academic benchmarks.",
    year: 2023,
    venue: "arXiv",
    citationCount: 12000,
    externalId: "arXiv:2303.08774",
  },
  {
    paperId: "4",
    title: "ImageNet Classification with Deep Convolutional Neural Networks",
    authors: [
      { authorId: "8", name: "Alex Krizhevsky" },
      { authorId: "9", name: "Ilya Sutskever" },
      { authorId: "10", name: "Geoffrey Hinton" },
    ],
    abstract:
      "We trained a large, deep convolutional neural network to classify the 1.2 million high-resolution images in the ImageNet LSVRC-2010 contest into the 1000 different classes. On the test data, we achieved top-1 and top-5 error rates of 37.5% and 17.0%.",
    year: 2012,
    venue: "NeurIPS",
    citationCount: 120000,
    externalId: null,
  },
  {
    paperId: "5",
    title: "Deep Residual Learning for Image Recognition",
    authors: [
      { authorId: "11", name: "Kaiming He" },
      { authorId: "12", name: "Xiangyu Zhang" },
      { authorId: "13", name: "Shaoqing Ren" },
    ],
    abstract:
      "Deeper neural networks are more difficult to train. We present a residual learning framework to ease the training of networks that are substantially deeper than those used previously. We explicitly reformulate the layers as learning residual functions with reference to the layer inputs, instead of learning unreferenced functions.",
    year: 2016,
    venue: "CVPR",
    citationCount: 180000,
    externalId: "arXiv:1512.03385",
  },
  {
    paperId: "6",
    title: "Generative Adversarial Networks",
    authors: [
      { authorId: "14", name: "Ian Goodfellow" },
      { authorId: "15", name: "Jean Pouget-Abadie" },
    ],
    abstract:
      "We propose a new framework for estimating generative models via an adversarial process, in which we simultaneously train two models: a generative model G that captures the data distribution, and a discriminative model D that estimates the probability that a sample came from the training data rather than G.",
    year: 2014,
    venue: "NeurIPS",
    citationCount: 75000,
    externalId: "arXiv:1406.2661",
  },
  {
    paperId: "7",
    title: "Dropout: A Simple Way to Prevent Neural Networks from Overfitting",
    authors: [
      { authorId: "16", name: "Nitish Srivastava" },
      { authorId: "17", name: "Geoffrey Hinton" },
    ],
    abstract:
      "Deep neural networks with a large number of parameters are very powerful machine learning systems. However, overfitting is a serious problem in such networks. Dropout is a technique for addressing this problem.",
    year: 2014,
    venue: "JMLR",
    citationCount: 45000,
    externalId: null,
  },
  {
    paperId: "8",
    title: "Adam: A Method for Stochastic Optimization",
    authors: [
      { authorId: "18", name: "Diederik P. Kingma" },
      { authorId: "19", name: "Jimmy Ba" },
    ],
    abstract:
      "We introduce Adam, an algorithm for first-order gradient-based optimization of stochastic objective functions, based on adaptive estimates of lower-order moments.",
    year: 2015,
    venue: "ICLR",
    citationCount: 180000,
    externalId: "arXiv:1412.6980",
  },
  {
    paperId: "9",
    title: "U-Net: Convolutional Networks for Biomedical Image Segmentation",
    authors: [
      { authorId: "20", name: "Olaf Ronneberger" },
      { authorId: "21", name: "Philipp Fischer" },
    ],
    abstract:
      "There is large consent that successful training of deep networks requires many thousand annotated training samples. We present a network and training strategy that relies on the strong use of data augmentation.",
    year: 2015,
    venue: "MICCAI",
    citationCount: 85000,
    externalId: "arXiv:1505.04597",
  },
  {
    paperId: "10",
    title: "Word2Vec: Distributed Representations of Words and Phrases and their Compositionality",
    authors: [
      { authorId: "22", name: "Tomas Mikolov" },
      { authorId: "23", name: "Ilya Sutskever" },
    ],
    abstract:
      "Efficient distributed representations of words and phrases and their compositionality are presented. The representations combine the known sub-sampling method with a novel multi-task learning method.",
    year: 2013,
    venue: "NeurIPS",
    citationCount: 35000,
    externalId: "arXiv:1310.4546",
  },
];

const SEMANTIC_SCHOLAR_API_URL = "https://api.semanticscholar.org/graph/v1/paper/search";

/**
 * Search papers using Semantic Scholar API
 */
export async function searchPapers(
  filters: SearchFilters,
  limit: number = 10,
  offset: number = 0
): Promise<SearchResult> {
  const { query, yearFrom, yearTo, venue, minCitations, openAccessOnly } = filters;

  // Build query parameters
  const params = new URLSearchParams({
    query,
    fields: "title,authors,abstract,year,venue,citationCount,externalId,openAccessPdf",
    limit: limit.toString(),
    offset: offset.toString(),
  });

  // Add year filter
  if (yearFrom || yearTo) {
    if (yearFrom && yearTo) {
      params.append("year", `${yearFrom}-${yearTo}`);
    } else if (yearFrom) {
      params.append("year", `${yearFrom}-`);
    } else if (yearTo) {
      params.append("year", `-${yearTo}`);
    }
  }

  // Add venue filter
  if (venue) {
    params.append("venue", venue);
  }

  // Add citation filter
  if (minCitations && minCitations > 0) {
    params.append("minCitationCount", minCitations.toString());
  }

  // Add open access filter
  if (openAccessOnly) {
    params.append("openAccessPdf", "true");
  }

  try {
    const response = await fetch(`${SEMANTIC_SCHOLAR_API_URL}?${params.toString()}`, {
      headers: {
        "Accept": "application/json",
      },
    });

    if (!response.ok) {
      throw new Error(`API error: ${response.status}`);
    }

    const data = await response.json();

    return {
      total: data.total || 0,
      offset: data.offset || offset,
      nextOffset: data.nextOffset || null,
      papers: data.papers.map((paper: Record<string, unknown>) => ({
        paperId: paper.paperId as string,
        title: paper.title as string,
        authors: (paper.authors as Author[]) || [],
        abstract: paper.abstract as string | null,
        year: paper.year as number | null,
        venue: paper.venue as string | null,
        citationCount: paper.citationCount as number || 0,
        externalId: paper.externalId as string | null,
        url: (paper.openAccessPdf as { url?: string })?.url,
      })),
    };
  } catch (error) {
    console.error("Semantic Scholar API error, using mock data:", error);

    // Fallback to mock data
    const filteredPapers = MOCK_PAPERS.filter((paper) => {
      const matchesQuery =
        !query ||
        paper.title.toLowerCase().includes(query.toLowerCase()) ||
        paper.abstract?.toLowerCase().includes(query.toLowerCase()) ||
        paper.authors.some((a) => a.name.toLowerCase().includes(query.toLowerCase()));

      const matchesYear =
        (!yearFrom || (paper.year && paper.year >= yearFrom)) &&
        (!yearTo || (paper.year && paper.year <= yearTo));

      const matchesVenue = !venue || paper.venue?.toLowerCase().includes(venue.toLowerCase());

      const matchesCitations = !minCitations || paper.citationCount >= minCitations;

      return matchesQuery && matchesYear && matchesVenue && matchesCitations;
    });

    const paginatedPapers = filteredPapers.slice(offset, offset + limit);

    return {
      total: filteredPapers.length,
      offset,
      nextOffset: offset + limit < filteredPapers.length ? offset + limit : null,
      papers: paginatedPapers,
    };
  }
}

/**
 * Get paper by ID
 */
export async function getPaper(paperId: string): Promise<Paper | null> {
  try {
    const response = await fetch(
      `${SEMANTIC_SCHOLAR_API_URL}/${paperId}?fields=title,authors,abstract,year,venue,citationCount,externalId`,
      {
        headers: {
          Accept: "application/json",
        },
      }
    );

    if (!response.ok) {
      throw new Error(`API error: ${response.status}`);
    }

    const paper = await response.json();

    return {
      paperId: paper.paperId,
      title: paper.title,
      authors: paper.authors || [],
      abstract: paper.abstract,
      year: paper.year,
      venue: paper.venue,
      citationCount: paper.citationCount || 0,
      externalId: paper.externalId,
    };
  } catch (error) {
    console.error("Error fetching paper:", error);
    return null;
  }
}

/**
 * Get common venues for filtering
 */
export function getCommonVenues(): string[] {
  return [
    "NeurIPS",
    "ICML",
    "ICLR",
    "ACL",
    "EMNLP",
    "NAACL",
    "COLING",
    "CVPR",
    "ICCV",
    "ECCV",
    "MICCAI",
    "AAAI",
    "IJCAI",
    "JMLR",
    "arXiv",
  ];
}
