# HtmlRAG: HTML is Better Than Plain Text for Modeling Retrieved Knowledge in RAG Systems

## Overview  
HtmlRAG revolutionizes Retrieval-Augmented Generation (RAG) by using HTML as the format for retrieved knowledge, rather than plain text. This approach preserves the structural and semantic information inherent in HTML documents, overcoming the limitations of traditional plain-text-based RAG systems.

---

## Key Features  

### 1. **HTML as Knowledge Format**  
Unlike traditional RAG systems that strip HTML to plain text, HtmlRAG uses HTML to retain:  
- Structural elements (e.g., headings, tables).  
- Semantic tags (e.g., `<code>`, `<a>`).  
- Content hierarchy.  

### 2. **HTML Cleaning Module**  
Removes unnecessary tokens like:  
- CSS styles.  
- JavaScript.  
- Comments.  

This module reduces HTML size by approximately **94%** while preserving key information.

### 3. **HTML Pruning with Block Trees**  
#### a. **Building Block Trees**  
Transforms HTML's DOM tree into hierarchical blocks, optimizing pruning granularity.  

#### b. **Relevance-Based Pruning**  
Leverages embedding models to rank blocks by query relevance and prune irrelevant sections.  

#### c. **Fine-Grained Pruning**  
Refines pruned block trees further, ensuring optimal content extraction.

---

## Benefits  

- **Enhanced Contextual Understanding:**  
  Preserves HTML structure for better LLM comprehension.  
- **Pre-trained Compatibility:**  
  Most LLMs already understand HTML without additional fine-tuning.  
- **Scalability:**  
  Supports documents converted from diverse formats (e.g., PDF, Word).  

---

## Challenges and Solutions  

### **Challenges:**  
- Excessive tokens in raw HTML (average size: **80K tokens/document**).  
- Noisy or redundant content affecting LLM efficiency.

### **Solutions:**  
- **Cleaning Module:** Reduces HTML to **6%** of its original size.  
- **Pruning Module:** Maintains relevance while minimizing size.  

---

## Experimental Results  

### Datasets:  
Tested on **six QA datasets**, demonstrating superior performance over traditional plain-text-based RAG systems.

### Findings:  
- **Preserved Information:** Retains structural and semantic integrity.  
- **Improved Generation:** Outperforms baseline systems in QA tasks.  

---

## Code and Resources  

- **GitHub Repository:** [HtmlRAG on GitHub](https://github.com/plageon/HtmlRAG)  
- **Paper:** [HtmlRAG Research Paper](https://arxiv.org/abs/2411.02959)  

---

## Acknowledgments  

HtmlRAG was developed by Jiejun Tan and collaborators at Baichuan Intelligent Technology. Special thanks to the community and prior works that inspired this innovation.  

---
