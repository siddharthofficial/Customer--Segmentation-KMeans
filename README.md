#  Customer Segmentation using K-Means Clustering

This project applies **K-Means Clustering** to segment customers based on their **Annual Income** and **Spending Score**, enabling businesses to better understand and target different customer groups.

## 📌 Objective
The goal is to group similar customers together to:
- Identify high-value customers
- Understand spending behavior
- Enable targeted marketing strategies

---

## 📊 Dataset
- **Source**: [Mall Customer Segmentation Dataset](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial)
- **Features used**:
  - Annual Income (k$)
  - Spending Score (1–100)

---

## 🧠 Techniques Used
- K-Means Clustering (Unsupervised ML)
- Elbow Method to determine optimal K
- Silhouette Score to evaluate clustering quality
- Cluster visualization using Matplotlib 

---

## 🔍 Evaluation Metrics
- **Optimal Clusters (K):** 5 (based on Elbow Method)
- **Silhouette Score:** `0.5539` (indicates good cluster structure)
- **Inertia (WCSS):** `44448` (compact clustering)

---

## 📈 Cluster Insights & Business Recommendations

### ✅ Cluster 1 (🟩 Green — High Income, High Spending Score)
- **Insight**: These are our loyal and premium customers.
- **Recommendations**:
  - Upsell premium/luxury products.
  - Provide personalized services or early access to new items.
  - Focus on retention strategies (e.g., loyalty programs, exclusive discounts).

---

### ✅ Cluster 2 (🔵 Blue — High Income, Low Spending Score)
- **Insight**: These customers have money but don’t spend much — potential untapped value.
- **Recommendations**:
  - Launch targeted marketing campaigns (email, social media).
  - Investigate for product mismatch or customer dissatisfaction.
  - Offer personalized bundles to encourage spending.

---

### ✅ Cluster 3 (🟥 Red — Average Income, Average Spending Score)
- **Insight**: This is the mainstream segment, steady but not highly profitable.
- **Recommendations**:
  - Use combo offers, loyalty rewards, and cashback to increase spending.
  - Engage this group for testing new products or marketing strategies.

---

### ✅ Cluster 4 (🟧 Orange — Low Income, High Spending Score)
- **Insight**: Value-driven or aspirational buyers — they spend a lot relative to income.
- **Recommendations**:
  - Focus on affordable luxury or EMI-based options.
  - Build brand loyalty; provide emotional value in offerings.
  - Monitor default risk if offering credit.

---

### ✅ Cluster 5 (⬛ Black — Low Income, Low Spending Score)
- **Insight**: Least profitable group, possibly bargain seekers or less engaged customers.
- **Recommendations**:
  - Minimize acquisition cost.
  - Offer budget-friendly products and bulk deals.
  - Deprioritize heavy marketing unless aligned with brand goals.

---

##  Tools & Libraries
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib

---

##  Future Improvements
- Add more features like Age, Gender
- Apply PCA for dimensionality reduction
- Compare with Hierarchical Clustering or DBSCAN

---

## Files in This Repo
- `Customer_Segmentation_KMeans.ipynb` — Main notebook
- `README.md` — Project description
-  Mall Customer Segmentation Dataset

---

##  Author
**Siddharth Jain**  
Aspiring Data Analyst | Passionate about Business + Data  
[LinkedIn](https://www.linkedin.com/in/siddharth-jain-979a35253/)
