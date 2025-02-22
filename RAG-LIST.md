# List of RAG Tools and Benchmarks
---

## [1] **EasyRAG**

*Published Date: 14 Oct 2024*

<sub><i style="font-size: 1.3em; color: gray;">Authors: Zhangchi Feng, Dongdong Kuang, Zhongyuan Wang, Zhijie Nie, Yaowei Zheng, Richong Zhang</i></sub>

This paper presents EasyRAG, a simple, lightweight, and efficient retrieval-augmented generation framework for automated network operations. EasyRAG has three advantages namely, accurate question answering, simple deployment and efficient inference. 

📄 Paper: [EasyRAG](https://arxiv.org/abs/2410.10315)  || 
💻 Code: [Github Repository](https://github.com/BUAADreamer/EasyRAG) 

#### [More Information](./docs/EasyRAG/EasyRAG.md)
---


## [2] **Vision-based RAG**

*Published Date: 14 Oct 2024*

<sub><i style="font-size: 1.3em; color: gray;">Authors: Shi Yu, Chaoyue Tang, Bokai Xu, Junbo Cui, Junhao Ran, Yukun Yan, Zhenghao Liu, Shuo Wang, Xu Han, Zhiyuan Liu, Maosong Sun</i></sub>

This paper presents VisRAG, which embeds documents using a Vision Language Model (VLM) as an image for retrieval, enhancing the generation process. Compared to traditional text-based RAG, VisRAG maximizes retention of original data, avoiding information loss during parsing. It achieves a 25–39% end-to-end performance gain over traditional text-based RAG pipelines.

📄 Paper: [Vision-based RAG](https://arxiv.org/abs/2410.10594) || 
💻 Code: [Github Repository](https://github.com/OpenBMB/VisRAG) ||
🤗 Hugging Face: [Hugginface Model](https://huggingface.co/openbmb/VisRAG-Ret)


---

## [3] **FunnelRAG**

*Published Date: 14 Oct 2024*


<sub><i style="font-size: 1.3em; color: gray;">Authors: Xinping Zhao, Yan Zhong, Zetian Sun, Xinshuo Hu, Zhenyu Liu, Dongfang Li, Baotian Hu, Min Zhang</i></sub>

This paper presents a progressive retrieval paradigm with coarse-to-fine granularity for RAG, termed FunnelRAG. FunnelRAG achieves comparable retrieval performance with a nearly 40% reduction in time overhead.

📄 Paper: [FunnelRAG](https://arxiv.org/abs/2410.10293) || 
💻 Code: [Github Repository]()

---

## [4] **CoFE-RAG**

*Published Date: 16 Oct 2024*

<sub><i style="font-size: 1.3em; color: gray;">Authors: Jintao Liu, Ruixue Ding, Linhao Zhang, Pengjun Xie, Fie Huang</i></sub>

This paper presents CoFE-RAG, a Comprehensive Full-chain Evaluation framework that evaluates the entire RAG pipeline, including chunking, retrieval, reranking, and generation. CoFE-RAG provides insights into RAG systems' effectiveness across diverse data scenarios.

📄 Paper: [CoFE-RAG](https://arxiv.org/abs/2410.12248) || 
💻 Code: [Github Repository](https://github.com/Alibaba-NLP/CoFE-RAG) 

---

## [5] **RAG-based Spelling Correction**

*Published Date: 15 Oct 2024*

<sub><i style="font-size: 1.3em; color: gray;">Authors: Xuan Guo, Rohit Patki, Dante Everaert, Christopher Potts</i></sub>

This paper presents a RAG-based spelling correction approach for e-commerce applications. Product names are retrieved from a catalog and integrated into the context used by a fine-tuned language model for contextual spelling correction, improving results over a standalone model.

📄 Paper: [RAG-based Spelling Correction](https://arxiv.org/abs/2410.11655) || 
💻 Code: [Github Repository]()

---

## [6] **Multilingual RAG**

*Published Date: 17 Oct 2024*

<sub><i style="font-size: 1.3em; color: gray;">Authors: Nandan Thakur, Suleman Kazi, Ge Luo, Jimmy Lin, Amin Ahmad</i></sub>

This paper introduces MIRAGE-Bench, a standardized multilingual RAG benchmark for 18 languages on Wikipedia. Built with the MIRACL retrieval dataset, it supports multilingual generation evaluation, showing that proprietary and large open-source LLMs currently excel in multilingual RAG.

📄 Paper: [MIRAGE-Bench](https://arxiv.org/abs/2410.13716) || 
💻 Code: [Github Repository](https://github.com/vectara/mirage-bench)

---

## [7] **HEALTH-PARIKSHA**

*Published Date: 17 Oct 2024*

 <sub><i style="font-size: 1.3em; color: gray;">Authors: Varun Gumma, Anandhita Raghunath, Mohit Jain, Sunayana Sitaram</i></sub>

This paper assesses 24 LLMs on real-world data from Indian patients interacting with a medical chatbot in English and 4 Indic languages, showing significant performance variance, lower factual accuracy for Indic languages, and inconsistent performance of instruction-tuned models on Indic queries.

📄 Paper: [HEALTH-PARIKSHA](https://arxiv.org/abs/2410.13671) || 
💻 Code: [Github Repository]()

---

## [8] **MMed-RAG**

*Published Date: 16 Oct 2024*

<sub><i style="font-size: 1.3em; color: gray;">Authors: Peng Xia, Kangyu Zhu, Haoran Li, Tianze Wang, Weijia Shi, Sheng Wang, Linjun Zhang, James Zou, Huaxiu Yao </i></sub>

This paper introduces MMed-RAG, a versatile multimodal retrieval-augmented generation (RAG) system designed to enhance the factuality of Medical Large Vision-Language Models (Med-LVLMs). MMed-RAG incorporates a domain-aware retrieval mechanism, adaptive context selection, and preference fine-tuning to improve alignment and mitigate issues like factual hallucination. Experimental results across five medical datasets (radiology, ophthalmology, pathology) demonstrate that MMed-RAG improves factual accuracy by 43.8% in medical VQA and report generation tasks.

📄 Paper: [MMed-RAG](https://arxiv.org/abs/2410.13085) || 
💻 Code: [Github Repository](https://github.com/richard-peng-xia/MMed-RAG)

---

## [9] **RuleRAG**

*Published Date: 15 Oct 2024*

<sub><i style="font-size: 1.3em; color: gray;">Authors: Zhongwu Chen, Chengjin Xu, Dingmin Wang, Zhen Huang, Yong Dou, Jian Guo</i></sub>

This paper presents Rule-Guided RAG, introducing symbolic rules for in-context learning to guide retrievers in retrieving logically related documents. RuleRAG-ICL improves retrieval and generation accuracy, scales with document quantity, and generalizes for untrained rules.

📄 Paper: [RuleRAG](https://arxiv.org/abs/2410.22353) || 
💻 Code: [Github Repository]()

---

## [10] **ChunkRAG**

*Published Date: 25 Oct 2024*

<sub><i style="font-size: 1.3em; color: gray;">Authors: Ishneet Sukhvinder Singh, Ritvik Aggarwal, Ibrahim Allahverdiyev, Muhammad Taha, Aslihan Akalin, Kevin Zhu, Sean O'Brien</i></sub>

This paper introduces ChunkRAG, a novel chunk filtering method for RAG systems. ChunkRAG uses semantic chunking and relevance scoring to improve alignment with user queries, outperforming existing RAG models in filtering irrelevant content.

📄 Paper: [ChunkRAG](https://arxiv.org/abs/2410.19572) || 
💻 Code: [Github Repository](https://github.com/OpenBMB/VisRAG) ||
🤗 Hugging Face: [Hugging Face Model](https://huggingface.co/openbmb/VisRAG-Ret)

---

## [11] **AutoRAG**

*Published Date: 28 Oct 2024*

<sub><i style="font-size: 1.3em; color: gray;">Authors: Dongkyu Kim, Byoungwook Kim, Donggeon Han, Matouš Eibich</i></sub>

This paper introduces AutoRAG, a framework that automatically identifies suitable RAG modules for specific datasets. AutoRAG explores and approximates optimal RAG module combinations and is available as a Python library.

📄 Paper: [AutoRAG](https://arxiv.org/abs/2410.20878) || 
💻 Code: [Github Repository](https://github.com/Marker-Inc-Korea/AutoRAG_ARAGOG_Paper)

---

## [12] **LONG²RAG**

*Published Date: 30 Oct 2024*

<sub><i style="font-size: 1.3em; color: gray;">Authors: Zehan Qi, Rongwu Xu, Zhijiang Guo, Cunxiang Wang, Hao Zhang, Wei Xu</i></sub>

This paper introduces LONG²RAG, addressing the limitations of existing RAG benchmarks in evaluating long-context retrieval. It introduces the Key Point Recall (KPR) metric to measure LLMs’ integration of key points from retrieved documents in long-form responses.

📄 Paper: [LONG²RAG](https://arxiv.org/abs/2410.23000) || 
💻 Code: [Github Repository]()

---

## [13] **LongRAG**

*Published Date: 21 Jun 2024*

<sub><i style="font-size: 1.3em; color: gray;">Authors: Ziyan Jiang, Xueguang Ma, Wenhu Chen</i></sub>

This paper introduces LongRAG, a framework designed to address the imbalance between retrievers and readers in traditional RAG systems. By processing the entire Wikipedia corpus into 4K-token units, LongRAG significantly reduces the number of retrievals, improving performance. It achieves strong retrieval results with fewer top units, outperforming fully-trained models on the NQ and HotpotQA datasets. LongRAG also excels on non-Wikipedia datasets like Qasper and MultiFieldQA-en, demonstrating its effectiveness with long-context LLMs.

📄 Paper: [LongRAG](https://arxiv.org/abs/2406.15319) || 
💻 Code: [Github Repository](https://github.com/TIGER-AI-Lab/LongRAG) || Website: [LongRAG](https://tiger-ai-lab.github.io/LongRAG/)

---

## [15] **PipeRAG**

*Published Date: 8 Mar 2024*

<sub><i style="font-size: 1.3em; color: gray;">Authors: Wenqi Jiang, Shuai Zhang, Boran Han, Jie Wang, Bernie Wang, Tim Kraska</i></sub>

This paper presents PipeRAG, an algorithm-system co-design approach to reduce latency and improve generation quality in retrieval-augmented generation (RAG). PipeRAG integrates pipeline parallelism, flexible retrieval intervals, and a performance model to balance retrieval quality and latency. The system achieves up to 2.6× speedup in end-to-end generation latency while enhancing generation quality.

📄 Paper: [PipeRAG](https://arxiv.org/abs/2403.05676) || 💻 Code: [Github Repository]()

---

## [16] **SimRAG**

*Published Date: 23 Oct 2024*

This paper presents SimRAG, a self-training approach to adapt retrieval-augmented generation (RAG) systems to specialized domains like science and medicine. By fine-tuning large language models (LLMs) on domain-specific data and using synthetic question generation, SimRAG improves domain adaptation. Experiments across 11 datasets show that SimRAG outperforms baselines by 1.2%–8.6%.

📄 Paper: [SimRAG](https://arxiv.org/abs/2410.17952) || 💻 Code: [Github Repository]()

---

## [17] **DRAGIN**

*Published Date: 15 Mar 2024*

<sub><i style="font-size: 1.3em; color: gray;">Authors: Weihang Su, Yichen Tang, Qingyao Ai, Zhijing Wu, Yiqun Liu</i></sub>

This paper presents DRAGIN, a dynamic retrieval-augmented generation (RAG) framework that actively decides when and what to retrieve based on the real-time information needs of large language models (LLMs). DRAGIN overcomes limitations in existing dynamic RAG methods by enabling context-aware retrieval during text generation. Experimental results show superior performance on four knowledge-intensive generation tasks.

📄 Paper: [DRAGIN](https://arxiv.org/abs/2403.10081) || 💻 Code: [Github Repository](https://github.com/oneal2000/DRAGIN/tree/main)

---

## [18] **LightRAG**

*Published Date: 8 Oct 2024*

<sub><i style="font-size: 1.3em; color: gray;">Authors: Zirui Guo, Lianghao Xia, Yanhua Yu, Tu Ao, Chao Huang</i></sub>

LightRAG introduces a novel dual-level retrieval system that integrates graph structures into the text indexing and retrieval processes. By combining low-level and high-level knowledge retrieval with efficient vector-based graph structures, LightRAG significantly improves both retrieval accuracy and response time while maintaining contextual relevance. Experimental validation shows substantial improvements over existing methods. LightRAG is open-source and available at the provided GitHub link.

📄 Paper: [LightRAG](https://arxiv.org/abs/2410.05779) || 💻 Code: [Github Repository](https://github.com/HKUDS/LightRAG)

---

## [19] **Open-RAG**

*Published Date: 2 Oct 2024*

<sub><i style="font-size: 1.3em; font-size: 1.3em; color: gray;">Authors: Shayekh Bin Islam, Md Asib Rahman, K S M Tozammel Hossain, Enamul Hoque, Shafiq Joty, Md Rizwan Parvez</i></sub>

Open-RAG enhances the reasoning capabilities of Retrieval-Augmented Generation (RAG) using open-source large language models (LLMs) by converting a dense LLM into a parameter-efficient sparse mixture of experts (MoE) model. This model can handle complex reasoning tasks, including multi-hop queries, and navigate misleading distractors. The framework integrates external knowledge efficiently for accurate, contextually relevant responses. Open-RAG also introduces a hybrid adaptive retrieval method to balance performance and inference speed. Experimental results show that Open-RAG outperforms existing models like ChatGPT and Self-RAG. The code and models are open-source.

📄 Paper: [Open-RAG](https://arxiv.org/abs/2410.01782) || 💻 Code: [Github Repository](https://github.com/ShayekhBinIslam/openrag) || 🌐 Website: [Open-RAG Website](https://openragmoe.github.io/) || 🤗 Hugging Face: [Open-RAG Model](https://huggingface.co/shayekh/openrag_llama2_7b_8x135m)

---

## [20] **HybridRAG**

*Published Date: 9 Aug 2024*

<sub><i style="font-size: 1.3em; color: gray;">Authors: Bhaskarjit Sarmah, Benika Hall, Rohan Rao, Sunil Patel, Stefano Pasquali, Dhagash Mehta</i></sub>

This paper introduces HybridRAG, a novel approach that combines Knowledge Graph-based RAG techniques (GraphRAG) and Vector Retrieval-Augmented Generation (VectorRAG) for enhanced information extraction from financial documents, particularly earnings call transcripts. HybridRAG significantly improves both retrieval accuracy and answer generation, making it highly effective in complex document formats.

📄 Paper: [HybridRAG](https://arxiv.org/abs/2408.04948) || 
💻 Code: [Github Repository]()

---

## [21] **Self-RAG**

*Published Date: 17 Oct 2024*

<sub><i style="font-size: 1.3em; color: gray;">Authors: Akari Asai, Zeqiu Wu, Yizhong Wang, Avirup Sil, Hannaneh Hajishirzi</i></sub>

Self-RAG introduces a self-reflective framework for Retrieval-Augmented Generation (RAG) that improves the factuality and quality of responses generated by large language models (LLMs). It enables LLMs to adaptively retrieve relevant passages, generate responses, and reflect on the retrieved content as well as its own outputs using reflection tokens. This results in more accurate and contextually relevant answers, outperformed state-of-the-art models like ChatGPT and Llama2-chat in tasks such as open-domain QA, reasoning, and fact verification.

📄 Paper: [Self-RAG](https://arxiv.org/abs/2310.11511) || 
💻 Code: [Github Repository](https://github.com/XXXX)

---

## [22] **MemoRAG**

*Published Date: 9 Sep 2024*

<sub><i style="font-size: 1.3em; color: gray;">Authors: Hongjin Qian, Peitian Zhang, Zheng Liu, Kelong Mao, Zhicheng Dou</i></sub>

MemoRAG introduces a novel retrieval-augmented generation paradigm empowered by long-term memory. It employs a dual-system architecture where a light LLM creates global memory and clues retrieval tools to locate useful information, while an expressive LLM generates the final answer. This combination enhances MemoRAG's ability to handle tasks involving ambiguous or unstructured knowledge, outperforming traditional RAG systems across a variety of complex and straightforward tasks.

📄 Paper: [MemoRAG](https://arxiv.org/abs/2409.05591) || 
💻 Code: [Github Repository](https://github.com/XXXX)

---

## [23] **Block-Attention for Efficient RAG**

*Published Date: 14 Sep 2024*

<sub><i style="font-size: 1.3em; color: gray;">Authors: East Sun, Yan Wang, Lan Tian</i></sub>

Block-Attention introduces an attention mechanism designed to reduce inference latency and cost in Retrieval-Augmented Generation (RAG) scenarios. By dividing retrieved documents into discrete blocks and independently calculating key-value (KV) states for each block, Block-Attention reuses KV states from previously seen passages, significantly cutting down on computation overhead. The method reduces time to first token (TTFT) and floating point operations (FLOPs) by over 98%, making it highly efficient for RAG applications. Experiments show that Block-Attention achieves performance comparable to or superior to self-attention models.

📄 Paper: [Block-Attention](https://arxiv.org/abs/2409.15355) || 
💻 Code: [Github Repository](https://github.com/XXXX)

---

## [24] **CORAG**

*Published Date: 1 Nov 2024*

<sub><i style="font-size: 1.3em; color: gray;">Authors: Ziting Wang, Haitao Yuan, Wei Dong, Gao Cong, Feifei Li</i></sub>

CORAG introduces a novel cost-constrained retrieval optimization system to address key challenges in Retrieval-Augmented Generation (RAG). Unlike traditional methods that select chunks independently, CORAG considers the correlations between chunks and applies a Monte Carlo Tree Search (MCTS) framework to optimize chunk combinations. By integrating budget constraints into the chunk selection process, CORAG overcomes the non-monotonicity of chunk utility, providing tailored solutions for user queries. This approach improves performance by maximizing the relevance and utility of the retrieved information.

📄 Paper: [CORAG](https://arxiv.org/abs/2411.00744) || 
💻 Code: [Github Repository](https://github.com/XXXX)

---

## [25] **Multi-Head RAG (MRAG)**

*Published Date: 7 Jun 2024*

<sub><i style="font-size: 1.3em; color: gray;">Authors: Maciej Besta, Ales Kubicek, Roman Niggli, Robert Gerstenberger, Lucas Weitzendorf, Mingyuan Chi, Patrick Iff, Joanna Gajda, Piotr Nyczyk, Jürgen Müller, Hubert Niewiadomski, Marcin Chrapek, Michał Podstawski, Torsten Hoefler</i></sub>

Multi-Head RAG (MRAG) addresses the challenge of handling multi-aspect queries in Retrieval Augmented Generation by leveraging the multi-head attention layer in Transformers. Unlike standard RAG, which may struggle with retrieving documents that have diverse content, MRAG uses attention heads to capture various data aspects. This approach enables MRAG to fetch multi-aspect documents with greater accuracy, showing up to a 20% improvement in relevance over traditional RAG methods. MRAG is seamlessly compatible with existing RAG frameworks, benchmarking tools like RAGAS, and various data stores.

📄 Paper: [Multi-Head RAG (MRAG)](https://arxiv.org/abs/2406.05085) || 💻 Code: [GitHub Repository](https://github.com/spcl/MRAG)


## [26] HtmlRAG

*Published Date: 5 Nov 2024*

<sub><i style="font-size: 1.3em; color: gray;">Authors: Jiejun Tan, Zhicheng Dou, Wen Wang, Mang Wang, Weipeng Chen, Ji-Rong Wen</i></sub>

HtmlRAG redefines Retrieval-Augmented Generation (RAG) by leveraging the structural and semantic richness of HTML documents instead of plain text. Unlike conventional RAG systems that strip HTML to plain text, HtmlRAG retains critical features like headings and table structures to enhance knowledge representation.

To overcome the challenges posed by HTML content, such as additional tags, JavaScript, and CSS, HtmlRAG employs innovative cleaning, compression, and a two-step block-tree-based pruning method to remove irrelevant blocks while preserving essential data. This approach demonstrates superior performance on six QA datasets, showcasing HTML’s potential in RAG systems.

📄 Paper: [HtmlRAG](https://arxiv.org/abs/2411.02959) || 💻 Code: [GitHub Repository](https://github.com/plageon/HtmlRAG) || 🤗 Huggingface Model: [Hugging Face Collection](https://huggingface.co/collections/zstanjj/htmlrag-671f03af5c3da2e7b5371aa4)


#### [More Information](./docs/EasyRAG/EasyRAG.md)