# EasyRAG: Efficient Retrieval-Augmented Generation Framework for Network Automated Operations

## Introduction

**EasyRAG** is a simple, lightweight, and efficient **retrieval-augmented generation (RAG)** framework designed to optimize automated network operations. It provides a scalable solution for fast and accurate question answering, with a special focus on efficiency and low resource usage. EasyRAG achieves this by combining **dual-route sparse retrieval**, **LLM reranking**, and **efficient inference acceleration**.

## Key Advantages of EasyRAG

EasyRAG has three main advantages that differentiate it from traditional RAG systems:

1. **Accurate Question Answering**: 
    - The framework utilizes a straightforward RAG scheme that incorporates:
        1. **A specific data processing workflow**
        2. **Dual-route sparse retrieval for coarse ranking**
        3. **LLM Reranker for reranking**  
        4. **LLM-based answer generation and optimization**  
    - These design elements contributed to EasyRAG's success, achieving **first place** in the **GLM4 track** during the preliminary round and **second place** in the semifinals.

2. **Simple Deployment**: 
    - EasyRAG does not require any model fine-tuning, minimizes VRAM usage, and is easy to deploy, making it highly scalable.
    - The framework is built on **BM25 retrieval** and **BGE-reranker reranking**, providing flexibility in **search** and **generation strategies**, enabling custom implementations.

3. **Efficient Inference**: 
    - An efficient **inference acceleration scheme** has been developed to reduce inference latency across the **coarse ranking**, **reranking**, and **generation** processes.
    - This scheme can be applied plug-and-play to any component, maintaining accuracy while enhancing the efficiency of the entire RAG system.

## Image Overview

Below is an illustration from the official EasyRAG GitHub repository, which provides a visual overview of the EasyRAG architecture.

![EasyRAG Architecture](../../assets/Rag-images/Overview%20of%20EasyRAG.png)

*Image source: [EasyRAG GitHub Repository](https://github.com/BUAADreamer/EasyRAG)*

## Related Researches

Several noteworthy researchers have contributed to the field of RAG frameworks:

- **Weijie Liu**, **Peng Zhou**, **Zhiruo Wang**, **Zhe Zhao**, **Haotang Deng**, **Qi Ju** for their work on **FastBERT**.
- **Xiao Liu**, **Xiao Xia**, **Xiaohan Zhang**, and others for their contributions to **ChatGLM** and other large language models.
- **Liang Wang**, **Nan Yang**, **Furu Wei** for their work on **Query2Doc**, which introduces query expansion with large language models.

### Key to the Solution

The key to EasyRAG's success lies in its ability to combine **sparse retrieval** with **dense retrieval** techniques in a dual-route fashion. Additionally, the use of query rewriting and context compression ensures that retrieval is both accurate and efficient. The result is an **optimized generation process** that is faster, requires less memory, and is highly scalable.

## Experiment Design

### Experimental Setup

The authors conducted a series of experiments to test EasyRAG's efficiency and accuracy. They used two major types of evaluation:
1. **Preliminary Experiments**: Focused on optimizing data processing workflows, chunk parameters, and sorting strategies.
2. **Semi-Final Experiments**: Focused on fine-tuning query rewriting methods, document extension strategies, and performance metrics.

### Key Optimizations Tested

1. **Data Processing Workflow**: Missing data was supplemented to improve model performance.
2. **Chunk Parameters**: Adjusting overlap between chunks improved retrieval accuracy by 2 percentage points.
3. **Sorting Fusion Strategies**: Combining results from both sparse and dense retrieval methods resulted in better performance than individual routes.
4. **Query Rewriting and Prompt Types**: Simpler prompts were found to outperform more complex ones in terms of accuracy.

## Dataset Used

The paper does not explicitly mention the dataset, but based on the methods used, it likely involved standard retrieval-augmented generation datasets for question answering, such as **SQuAD** or **Natural Questions**.

## Code Availability

The paper does not specify whether the code is open-source. However, EasyRAG is designed to be easily deployable with minimal VRAM and supports various search and generation strategies.

## Contributions

1. **Accurate Question Answering**: EasyRAG achieves state-of-the-art accuracy by combining dual-route sparse retrieval and fine-tuned LLM reranking.
2. **Simple Deployment**: The system is designed to be easy to deploy with minimal configuration, making it suitable for real-time applications.
3. **Efficient Inference**: With its optimized inference acceleration, EasyRAG significantly reduces latency during query processing.
4. **Scalability**: EasyRAG can handle multiple RAG processes simultaneously, making it ideal for large-scale applications.

## Future Work

Future research could focus on the following areas:

1. **Further Optimizing Retrieval**: Exploring more efficient retrieval methods and fine-tuning query rewriting techniques could enhance accuracy further.
2. **Utilizing Image Information**: Integrating image retrieval into the framework could provide multimodal capabilities and improve retrieval.
3. **Improving Answer Integration**: Developing more sophisticated methods for integrating answers from multiple sources could lead to more comprehensive responses.

## Conclusion

EasyRAG introduces a new approach to retrieval-augmented generation by focusing on **efficiency**, **scalability**, and **low resource usage**. By leveraging dual-route retrieval, query rewriting, and context compression, EasyRAG is able to deliver high performance while being suitable for real-time and resource-constrained environments.

---

## Acknowledgments

This summary is based on research and information gathered from various sources, including academic papers, blog posts, and tutorials on retrieval-augmented generation. Special thanks to the original authors of **EasyRAG** for their groundbreaking work.

- Weijie Liu, Peng Zhou, Zhiruo Wang, Zhe Zhao, Haotang Deng, Qi Ju for **FastBERT**
- Xiao Liu, Xiao Xia, Xiaohan Zhang, and others for **ChatGLM**
- Liang Wang, Nan Yang, Furu Wei for **Query2Doc**

---

This structure ensures that the core aspects of EasyRAG are clearly explained, while also including the new information about the framework's advantages and the image. You can replace the image path with the actual location if available. Let me know if you need further changes or enhancements!
