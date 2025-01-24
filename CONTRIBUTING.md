# Contributing to RAGpedia

Thank you for your interest in contributing to **RAGpedia**! Your efforts make this repository a comprehensive and valuable resource for RAG tools, benchmarks, and learning materials. Whether you're adding tools, tutorials, or improving documentation, your contributions help the RAG community thrive.

## How to Contribute

### 1. Adding New Tools or Benchmarks

To add a new RAG tool or benchmark:

1. **Edit `RAG-LIST.md`**:  
   Add an entry with the following details:
   - **Name**: The name of the tool or benchmark.
   - **Description**: A short summary of its functionality.
   - **Discoverer**: The name(s) of the primary authors or discoverers.
   - **GitHub Repository Link**: URL to the tool’s GitHub repository, if available.
   - **Paper Link**: URL to the research paper or documentation.

2. **Use the Template Below**:  
   Ensure your entry follows this format for consistency:

   ```markdown
   - **[Tool Name](GitHub Link)**  
     _Discoverer_: Author(s)  
     **Description**: Short description here  
     📄 [Paper Link](URL) | 💻 [GitHub Repository](URL)
   ```

   **Example**:  

   ```markdown
   - **[AwesomeRAG](https://github.com/example/AwesomeRAG)**  
     _Discoverer_: Dr. John Doe  
     **Description**: A cutting-edge retrieval-augmented generation tool for text summarization.  
     📄 [Paper Link](https://example.com/paper) | 💻 [GitHub Repository](https://github.com/example/AwesomeRAG)
   ```

3. **Submit a Pull Request (PR)**:  
   Once you've added the tool, create a PR with a clear title (e.g., "Added AwesomeRAG to RAG-LIST.md"). Our team will review your submission and may request minor changes.

---

### 2. Adding Tutorials and Learning Resources

You can contribute tutorial code or Jupyter Notebooks (IPYNB) to help others learn about RAG tools.

1. **Organize Your Tutorial**:  
   - Place all tutorial files in the `tutorials` folder. If the folder doesn’t exist, create it.
   - Add detailed comments or markdown cells to explain each step, theory, setup instructions, and usage examples.

2. **Update the Tutorials Index**:  
   Create or update a `README.md` file in the `tutorials` folder with:
   - A short summary of your tutorial.
   - A link to your tutorial file.

   **Example**:  

   ```markdown
   ## Tutorials

   - **[Getting Started with RAG](tutorials/getting_started.ipynb)**  
     Learn the basics of retrieval-augmented generation with this beginner-friendly tutorial.
   ```

3. **Submit a PR**:  
   Once your tutorial is ready, create a PR and include details about what your tutorial covers.

---

### 3. Improving Documentation

Help us keep our documentation clear, accurate, and beginner-friendly:

- **Clarify Explanations**: Add examples, diagrams, or detailed explanations to make content easier to understand.
- **Update Information**: Correct outdated details about tools or benchmarks.
- **Fix Errors**: Address typos, grammar mistakes, or formatting issues.
- **Add Examples**: Include examples for added clarity.

---

### 4. Suggestions and Feature Requests

If you have an idea but aren’t sure how to implement it, open an **issue** in the repository. Include:

- A clear title summarizing your suggestion.
- A detailed description of your idea and how it can improve RAGpedia.

Our team will review and discuss your suggestion with you.

---

## Frequently Asked Questions (FAQ)

**Q: How do I fork and clone the repository?**  
A:  

1. Click the **Fork** button at the top right of the RAGpedia repository.  
2. Clone your fork locally using:  

   ```bash
   git clone https://github.com/<your-username>/RAGpedia.git
   ```

**Q: What if my PR gets rejected?**  
A: Don't worry! We'll provide constructive feedback so you can make necessary changes and resubmit your PR.

**Q: Do I need prior experience with RAG to contribute?**  
A: Not at all! We welcome contributions from all skill levels. If you're new, consider starting with documentation or tutorials.

**Q: Can I add tools that aren’t hosted on GitHub?**  
A: Yes! Just ensure you provide a valid source link, such as a research paper or official documentation.

---

## Code of Conduct

Please follow our [Code of Conduct](CODE_OF_CONDUCT.md) to maintain a respectful and welcoming environment for all contributors.

---

## Licensing

By contributing to RAGpedia, you agree that your contributions will be licensed under the [MIT License](LICENSE), allowing free use, distribution, and modification of all resources within the repository.

---

Thank you for helping build RAGpedia into a valuable resource for the RAG community. Your contributions matter!

---

## Related Information from README.md

For detailed insights into the purpose and contents of RAGpedia, please refer to the [README.md](README.md) file. Highlights include:

- **Centralized Knowledge**: Information on RAG tools and benchmarks.
- **Accessibility**: Resources for researchers, developers, and learners.
- **Community Contributions**: Encouraging collaborative growth.

We extend our gratitude to all contributors and users, as well as the researchers and developers who create and share RAG models and benchmarks. Together, we can help make RAGpedia a resource that benefits the entire community.
