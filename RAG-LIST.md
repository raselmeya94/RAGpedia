# List of RAG Tools and Benchmarks
---

## [1] **EasyRAG**

<sub><i style="font-size: 1.3em; color: gray;">Authors: Zhangchi Feng, Dongdong Kuang, Zhongyuan Wang, Zhijie Nie, Yaowei Zheng, Richong Zhang</i></sub>

This paper presents EasyRAG, a simple, lightweight, and efficient retrieval-augmented generation framework for automated network operations. EasyRAG has three advantages namely, accurate question answering, simple deployment and efficient inference. 

📄 Paper: [EasyRAG](https://arxiv.org/abs/2410.10315)  || 
💻 Code: [Github Repository](https://github.com/BUAADreamer/EasyRAG) 

---


## [2] **Vision-based RAG**

<sub><i style="font-size: 1.3em; color: gray;">Authors: Shi Yu, Chaoyue Tang, Bokai Xu, Junbo Cui, Junhao Ran, Yukun Yan, Zhenghao Liu, Shuo Wang, Xu Han, Zhiyuan Liu, Maosong Sun</i></sub>

This paper presents VisRAG, which embeds documents using a Vision Language Model (VLM) as an image for retrieval, enhancing the generation process. Compared to traditional text-based RAG, VisRAG maximizes retention of original data, avoiding information loss during parsing. It achieves a 25–39% end-to-end performance gain over traditional text-based RAG pipelines.

📄 Paper: [Vision-based RAG](https://arxiv.org/abs/2410.10594) || 
💻 Code: [Github Repository](https://github.com/OpenBMB/VisRAG) ||
🤗 Hugging Face: [Hugginface Model](https://huggingface.co/openbmb/VisRAG-Ret)


---

## [3] **FunnelRAG**

<sub><i style="font-size: 1.3em; color: gray;">Authors: Xinping Zhao, Yan Zhong, Zetian Sun, Xinshuo Hu, Zhenyu Liu, Dongfang Li, Baotian Hu, Min Zhang</i></sub>

This paper presents a progressive retrieval paradigm with coarse-to-fine granularity for RAG, termed FunnelRAG. FunnelRAG achieves comparable retrieval performance with a nearly 40% reduction in time overhead.

📄 Paper: [FunnelRAG](https://arxiv.org/abs/2410.10293) || 
💻 Code: [Github Repository]()

---

## [4] **CoFE-RAG**

<sub><i style="font-size: 1.3em; color: gray;">Authors: Jintao Liu, Ruixue Ding, Linhao Zhang, Pengjun Xie, Fie Huang</i></sub>

This paper presents CoFE-RAG, a Comprehensive Full-chain Evaluation framework that evaluates the entire RAG pipeline, including chunking, retrieval, reranking, and generation. CoFE-RAG provides insights into RAG systems' effectiveness across diverse data scenarios.

📄 Paper: [CoFE-RAG](https://arxiv.org/abs/2410.12248) || 
💻 Code: [Github Repository](https://github.com/Alibaba-NLP/CoFE-RAG) 

---

## [5] **RAG-based Spelling Correction**

<sub><i style="font-size: 1.3em; color: gray;">Authors: Xuan Guo, Rohit Patki, Dante Everaert, Christopher Potts</i></sub>

This paper presents a RAG-based spelling correction approach for e-commerce applications. Product names are retrieved from a catalog and integrated into the context used by a fine-tuned language model for contextual spelling correction, improving results over a standalone model.

📄 Paper: [RAG-based Spelling Correction](https://arxiv.org/abs/2410.11655) || 
💻 Code: [Github Repository]()

---

## [6] **Multilingual RAG Benchmark**

<sub><i style="font-size: 1.3em; color: gray;">Authors: Nandan Thakur, Suleman Kazi, Ge Luo, Jimmy Lin, Amin Ahmad</i></sub>

This paper introduces MIRAGE-Bench, a standardized multilingual RAG benchmark for 18 languages on Wikipedia. Built with the MIRACL retrieval dataset, it supports multilingual generation evaluation, showing that proprietary and large open-source LLMs currently excel in multilingual RAG.

📄 Paper: [MIRAGE-Bench](https://arxiv.org/abs/2410.13716) || 
💻 Code: [Github Repository](https://github.com/vectara/mirage-bench)

---

## [7] **Assessing RAG Models for Health Chatbots**

 <sub><i style="font-size: 1.3em; color: gray;">Authors: Varun Gumma, Anandhita Raghunath, Mohit Jain, Sunayana Sitaram</i></sub>

This paper assesses 24 LLMs on real-world data from Indian patients interacting with a medical chatbot in English and 4 Indic languages, showing significant performance variance, lower factual accuracy for Indic languages, and inconsistent performance of instruction-tuned models on Indic queries.

📄 Paper: [HEALTH-PARIKSHA](https://arxiv.org/abs/2410.13671) || 
💻 Code: [Github Repository]()

---

## [8] **Medical Multimodal RAG System**

<sub><i style="font-size: 1.3em; color: gray;">Authors: Peng Xia, Kangyu Zhu, Haoran Li, Tianze Wang, Weijia Shi, Sheng Wang, Linjun Zhang, James Zou, Huaxiu Yao </i></sub>

This paper introduces MMed-RAG, a versatile multimodal retrieval-augmented generation (RAG) system designed to enhance the factuality of Medical Large Vision-Language Models (Med-LVLMs). MMed-RAG incorporates a domain-aware retrieval mechanism, adaptive context selection, and preference fine-tuning to improve alignment and mitigate issues like factual hallucination. Experimental results across five medical datasets (radiology, ophthalmology, pathology) demonstrate that MMed-RAG improves factual accuracy by 43.8% in medical VQA and report generation tasks.

📄 Paper: [MMed-RAG](https://arxiv.org/abs/2410.13085) || 
💻 Code: [Github Repository](https://github.com/richard-peng-xia/MMed-RAG)

---

## [9] **RuleRAG**

<sub><i style="font-size: 1.3em; color: gray;">Authors: Zhongwu Chen, Chengjin Xu, Dingmin Wang, Zhen Huang, Yong Dou, Jian Guo</i></sub>

This paper presents Rule-Guided RAG, introducing symbolic rules for in-context learning to guide retrievers in retrieving logically related documents. RuleRAG-ICL improves retrieval and generation accuracy, scales with document quantity, and generalizes for untrained rules.

📄 Paper: [RuleRAG](https://arxiv.org/abs/2410.22353) || 
💻 Code: [Github Repository]()

---

## [10] **ChunkRAG**

<sub><i style="font-size: 1.3em; color: gray;">Authors: Ishneet Sukhvinder Singh, Ritvik Aggarwal, Ibrahim Allahverdiyev, Muhammad Taha, Aslihan Akalin, Kevin Zhu, Sean O'Brien</i></sub>

This paper introduces ChunkRAG, a novel chunk filtering method for RAG systems. ChunkRAG uses semantic chunking and relevance scoring to improve alignment with user queries, outperforming existing RAG models in filtering irrelevant content.

📄 Paper: [ChunkRAG](https://arxiv.org/abs/2410.19572) || 
💻 Code: [Github Repository](https://github.com/OpenBMB/VisRAG) ||
🤗 Hugging Face: [Hugging Face Model](https://huggingface.co/openbmb/VisRAG-Ret)

---

## [11] **AutoRAG Framework**

<sub><i style="font-size: 1.3em; color: gray;">Authors: Dongkyu Kim, Byoungwook Kim, Donggeon Han, Matouš Eibich</i></sub>

This paper introduces AutoRAG, a framework that automatically identifies suitable RAG modules for specific datasets. AutoRAG explores and approximates optimal RAG module combinations and is available as a Python library.

📄 Paper: [AutoRAG](https://arxiv.org/abs/2410.20878) || 
💻 Code: [Github Repository](https://github.com/Marker-Inc-Korea/AutoRAG_ARAGOG_Paper)

---

## [12] **LONG²RAG**

<sub><i style="font-size: 1.3em; color: gray;">Authors: Zehan Qi, Rongwu Xu, Zhijiang Guo, Cunxiang Wang, Hao Zhang, Wei Xu</i></sub>

This paper introduces LONG²RAG, addressing the limitations of existing RAG benchmarks in evaluating long-context retrieval. It introduces the Key Point Recall (KPR) metric to measure LLMs’ integration of key points from retrieved documents in long-form responses.

📄 Paper: [LONG²RAG](https://arxiv.org/abs/2410.23000) || 
💻 Code: [Github Repository]()

---

## [13] **LongRAG**

<sub><i style="font-size: 1.3em; color: gray;">Authors: Ziyan Jiang, Xueguang Ma, Wenhu Chen</i></sub>

This paper introduces LongRAG, a framework designed to address the imbalance between retrievers and readers in traditional RAG systems. By processing the entire Wikipedia corpus into 4K-token units, LongRAG significantly reduces the number of retrievals, improving performance. It achieves strong retrieval results with fewer top units, outperforming fully-trained models on the NQ and HotpotQA datasets. LongRAG also excels on non-Wikipedia datasets like Qasper and MultiFieldQA-en, demonstrating its effectiveness with long-context LLMs.

📄 Paper: [LongRAG](https://arxiv.org/abs/2406.15319) || 
💻 Code: [Github Repository](https://github.com/TIGER-AI-Lab/LongRAG) || Website: [LongRAG](https://tiger-ai-lab.github.io/LongRAG/)

---

## [15] **PipeRAG**

<sub><i style="font-size: 1.3em; color: gray;">Authors: Wenqi Jiang, Shuai Zhang, Boran Han, Jie Wang, Bernie Wang, Tim Kraska</i></sub>

This paper presents PipeRAG, an algorithm-system co-design approach to reduce latency and improve generation quality in retrieval-augmented generation (RAG). PipeRAG integrates pipeline parallelism, flexible retrieval intervals, and a performance model to balance retrieval quality and latency. The system achieves up to 2.6× speedup in end-to-end generation latency while enhancing generation quality.

📄 Paper: [PipeRAG](https://arxiv.org/abs/2403.05676) || 💻 Code: [Github Repository]()

---

## [16] **SimRAG**

This paper presents SimRAG, a self-training approach to adapt retrieval-augmented generation (RAG) systems to specialized domains like science and medicine. By fine-tuning large language models (LLMs) on domain-specific data and using synthetic question generation, SimRAG improves domain adaptation. Experiments across 11 datasets show that SimRAG outperforms baselines by 1.2%–8.6%.

📄 Paper: [SimRAG](https://arxiv.org/abs/2410.17952) || 💻 Code: [Github Repository]()

---

## [17] **DRAGIN**

<sub><i style="font-size: 1.3em; color: gray;">Authors: Weihang Su, Yichen Tang, Qingyao Ai, Zhijing Wu, Yiqun Liu</i></sub>

This paper presents DRAGIN, a dynamic retrieval-augmented generation (RAG) framework that actively decides when and what to retrieve based on the real-time information needs of large language models (LLMs). DRAGIN overcomes limitations in existing dynamic RAG methods by enabling context-aware retrieval during text generation. Experimental results show superior performance on four knowledge-intensive generation tasks.

📄 Paper: [DRAGIN](https://arxiv.org/abs/2403.10081) || 💻 Code: [Github Repository](https://github.com/oneal2000/DRAGIN/tree/main)

---

## [18] **LightRAG**

<sub><i style="font-size: 1.3em; color: gray;">Authors: Zirui Guo, Lianghao Xia, Yanhua Yu, Tu Ao, Chao Huang</i></sub>

LightRAG introduces a novel dual-level retrieval system that integrates graph structures into the text indexing and retrieval processes. By combining low-level and high-level knowledge retrieval with efficient vector-based graph structures, LightRAG significantly improves both retrieval accuracy and response time while maintaining contextual relevance. Experimental validation shows substantial improvements over existing methods. LightRAG is open-source and available at the provided GitHub link.

📄 Paper: [LightRAG](https://arxiv.org/abs/2410.05779) || 💻 Code: [Github Repository](https://github.com/HKUDS/LightRAG)

---

## [19] **Open-RAG**

<sub><i style="font-size: 1.3em; font-size: 1.3em; color: gray;">Authors: Shayekh Bin Islam, Md Asib Rahman, K S M Tozammel Hossain, Enamul Hoque, Shafiq Joty, Md Rizwan Parvez</i></sub>

Open-RAG enhances the reasoning capabilities of Retrieval-Augmented Generation (RAG) using open-source large language models (LLMs) by converting a dense LLM into a parameter-efficient sparse mixture of experts (MoE) model. This model can handle complex reasoning tasks, including multi-hop queries, and navigate misleading distractors. The framework integrates external knowledge efficiently for accurate, contextually relevant responses. Open-RAG also introduces a hybrid adaptive retrieval method to balance performance and inference speed. Experimental results show that Open-RAG outperforms existing models like ChatGPT and Self-RAG. The code and models are open-source.

📄 Paper: [Open-RAG](https://arxiv.org/abs/2410.01782) || 💻 Code: [Github Repository](https://github.com/ShayekhBinIslam/openrag) || 🌐 Website: [Open-RAG Website](https://openragmoe.github.io/) || 🤗 Hugging Face: [Open-RAG Model](https://huggingface.co/shayekh/openrag_llama2_7b_8x135m)

---
