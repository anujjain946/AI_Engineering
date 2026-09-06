# SVM + Naive Bayes

Complete notes for **Support Vector Machine (SVM)** and **Naive Bayes**, including concepts, formulas, examples, Python implementation, and interview revision.

---

# 1. Support Vector Machine (SVM)

## What is SVM?

**Support Vector Machine** ek supervised machine learning algorithm hai jo mainly classification problems ke liye use hota hai.

SVM ka main goal:

> Classes ko separate karne wali best decision boundary find karna, jiska **margin maximum** ho.

### Example

Suppose hume customers ko classify karna hai:

```text
0 = Customer will stay
1 = Customer will churn
```

Features:

```text
Tenure
MonthlyCharges
```

SVM in features ke basis par ek decision boundary find karega.

---

# 2. Hyperplane

## What is Hyperplane?

**Hyperplane** wo decision boundary hai jo different classes ko separate karti hai.

2D case mein hyperplane ek straight line hoti hai.

Formula:

```text
w1*x1 + w2*x2 + b = 0
```

Where:

```text
w1, w2 = weights
x1, x2 = features
b = bias
```

### Example

```text
Monthly Charges

    ● ● ●
   ● ●
       ●

--------------------  ← Hyperplane

          ▲ ▲
        ▲ ▲ ▲
       ▲
       
                 Tenure
```

Upper side ke customers ek class ho sakte hain aur lower side ke customers doosri class.

### Simple Trick

> **Hyperplane = Decision Boundary**

---

# 3. Support Vectors

## What are Support Vectors?

Decision boundary ke sabse close data points ko **Support Vectors** kehte hain.

Example:

```text
        ●
        
        ●  ← Support Vector

--------------------  ← Hyperplane

        ▲  ← Support Vector
        
        ▲
```

Ye points SVM ke liye important hote hain because ye decision boundary ko determine karte hain.

### Simple Trick

> **Boundary ke paas = Support Vector**

---

# 4. Margin

## What is Margin?

Hyperplane aur nearest support vectors ke beech ka distance **Margin** kehlata hai.

```text
Support Vector
      ●
      |
      | ← Margin
      |
------|------------- Hyperplane
      |
      | ← Margin
      |
      ▲
Support Vector
```

SVM ka goal:

> **Maximum Margin**

### Why Maximum Margin?

Large margin generally model ko unseen data par better generalize karne mein help karta hai.

### Simple Trick

> **SVM = Maximum Margin Machine**

---

# 5. Hard Margin

Hard Margin SVM tab use hota hai jab data perfectly linearly separable ho.

Example:

```text
● ● ●

● ●

----------------

▲ ▲

▲ ▲ ▲
```

No data point boundary ke wrong side nahi hona chahiye.

### Problem

Real-world data usually perfectly separable nahi hota.

Isliye practical problems mein **Soft Margin** zyada useful hota hai.

---

# 6. Soft Margin

Soft Margin SVM kuch misclassification ko tolerate karta hai.

Example:

```text
● ●
  ●

      ▲

----------- Boundary -----------

●

        ▲ ▲
```

Ye real-world noisy data ke liye useful hai.

Soft margin ko control karne ke liye important parameter:

```text
C
```

---

# 7. C Parameter

## What is C?

`C` decide karta hai ki model training errors ko kitna punish karega.

### High C

```text
High C
   ↓
Mistake ki high penalty
   ↓
Training data ko closely fit
   ↓
Smaller margin
   ↓
Overfitting ka risk
```

### Low C

```text
Low C
   ↓
Mistake ki low penalty
   ↓
More errors tolerate
   ↓
Larger margin
   ↓
Better generalization possible
```

### Example

Suppose:

```text
C = 100
```

Model mistakes avoid karne ke liye strongly try karega.

Agar:

```text
C = 0.1
```

Model larger margin prefer karega, even if kuch points misclassified ho jayein.

### Memory Trick

> **C = Cost of mistake**

Remember:

```text
High C → Less mistakes → Narrow margin

Low C → More tolerance → Wide margin
```

---

# 8. Kernel

## Why do we need Kernel?

Kabhi-kabhi data straight line se separate nahi ho sakta.

Example:

```text
        ● ●
      ●     ●

       ▲ ▲
      ▲   ▲
```

Aisi situation mein linear boundary kaam nahi karegi.

SVM **Kernel** ka use karke complex/non-linear decision boundary create kar sakta hai.

### Simple Trick

> **Kernel = Non-linear boundary ko handle karne ka method**

---

# 9. Types of Kernels

## 9.1 Linear Kernel

Simple linear data ke liye.

```python
from sklearn.svm import SVC

model = SVC(kernel="linear")
```

Use when:

```text
Data approximately linearly separable hai
```

---

## 9.2 Polynomial Kernel

Curved decision boundary ke liye.

```python
model = SVC(kernel="poly")
```

Polynomial degree bhi control kar sakte hain.

```python
model = SVC(
    kernel="poly",
    degree=3
)
```

---

## 9.3 RBF Kernel

RBF = Radial Basis Function

Complex non-linear data ke liye commonly used kernel.

```python
model = SVC(kernel="rbf")
```

RBF ke saath `gamma` important parameter hai.

---

## 9.4 Sigmoid Kernel

Sigmoid-based decision boundary.

```python
model = SVC(kernel="sigmoid")
```

Practical ML problems mein Linear aur RBF kernels commonly encountered hote hain.

---

# 10. Gamma

## What is Gamma?

`gamma` mainly RBF kernel mein important hota hai.

Gamma control karta hai:

> Ek individual training point ka influence kitni range tak hoga.

---

## Low Gamma

Low gamma ka matlab:

```text
Point ka influence
       ↓
Large area
       ↓
Smoother boundary
```

Potential risk:

```text
Underfitting
```

---

## High Gamma

High gamma:

```text
Point ka influence
       ↓
Small/local area
       ↓
Complex boundary
```

Potential risk:

```text
Overfitting
```

### Memory Trick

> **Gamma = Reach**

```text
Low Gamma  → Long Reach

High Gamma → Short Reach
```

---

# 11. C vs Gamma

Ye interview mein bahut important comparison hai.

| Parameter | Controls                      |
| --------- | ----------------------------- |
| `C`       | Misclassification ki penalty  |
| `gamma`   | Individual point ka influence |

### Memory Trick

```text
C      = Mistake ka Cost
Gamma  = Point ka Reach
```

---

# 12. Complete SVM Example

Suppose:

```text
X = Customer features

X1 = Tenure
X2 = MonthlyCharges

y = Churn
```

Python:

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = SVC(
    kernel="rbf",
    C=1.0,
    gamma="scale"
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
```

### Why Scaling?

SVM distance and margin concepts par depend karta hai.

Agar:

```text
Age = 20 - 80
Salary = 20000 - 200000
```

to salary feature ka scale bahut large hai.

Isliye SVM ke liye **feature scaling usually important** hoti hai.

---

# 13. Naive Bayes

## What is Naive Bayes?

Naive Bayes ek probabilistic classification algorithm hai.

Ye:

```text
Bayes Theorem
+
Conditional Independence Assumption
```

par based hai.

---

# 14. Bayes Theorem

Formula:

```text
P(A|B) = P(B|A) * P(A) / P(B)
```

Where:

```text
P(A|B) = Posterior probability
P(B|A) = Likelihood
P(A)   = Prior probability
P(B)   = Evidence
```

---

# 15. Simple Bayes Example

Suppose:

```text
A = Customer will churn
B = Customer has month-to-month contract
```

We want:

```text
P(Churn | MonthToMonth)
```

Meaning:

> Agar customer ka contract month-to-month hai, to churn karne ki probability kya hai?

Bayes theorem:

```text
P(Churn | MonthToMonth)

=
P(MonthToMonth | Churn)
*
P(Churn)
/
P(MonthToMonth)
```

---

# 16. Why "Naive"?

Naive Bayes assume karta hai ki features class ke given **conditionally independent** hain.

Example:

```text
Age
Tenure
MonthlyCharges
Contract
PaymentMethod
```

Model approximately assume karta hai ki:

```text
Age
Tenure
MonthlyCharges
Contract
PaymentMethod
```

class ke context mein independent evidence ki tarah behave karte hain.

Real-world data mein ye assumption perfectly true nahi hoti.

Phir bhi Naive Bayes kaafi problems mein effective hota hai.

### Memory Trick

> **Naive = Independence Assumption**

---

# 17. Gaussian Naive Bayes

## When to use?

Continuous numerical features ke liye.

Examples:

```text
Age = 32
Salary = 55000
Tenure = 18.5
MonthlyCharges = 72.5
```

Gaussian NB assume karta hai ki continuous features approximately normal/Gaussian distribution follow karte hain.

### Python

```python
from sklearn.naive_bayes import GaussianNB

model = GaussianNB()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
```

### Memory Trick

> **Gaussian = Numbers**

---

# 18. Multinomial Naive Bayes

## When to use?

Count/frequency based features ke liye.

Especially:

```text
Text Classification
Spam Detection
Document Classification
Sentiment Analysis
```

Example:

Text:

```text
"good good service"
```

Word counts:

```text
good = 2
service = 1
```

Multinomial NB in counts ko use kar sakta hai.

### Python

```python
from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()

model.fit(X_train, y_train)
```

### Memory Trick

> **Multinomial = Counts**

---

# 19. Bernoulli Naive Bayes

## When to use?

Binary features ke liye.

Examples:

```text
0 / 1
Yes / No
True / False
Present / Absent
```

Customer example:

```text
HasInternet = 1
HasComplaint = 0
HasContract = 1
```

### Python

```python
from sklearn.naive_bayes import BernoulliNB

model = BernoulliNB()

model.fit(X_train, y_train)
```

### Memory Trick

> **Bernoulli = Binary**

---

# 20. Gaussian vs Multinomial vs Bernoulli

| Model         | Data Type            | Example     | Memory Trick |
| ------------- | -------------------- | ----------- | ------------ |
| GaussianNB    | Continuous numerical | Age, Salary | Numbers      |
| MultinomialNB | Counts/Frequencies   | Word counts | Counts       |
| BernoulliNB   | Binary               | 0/1, Yes/No | Binary       |

### Super Trick

> **G-M-B = Numbers → Counts → Binary**

---

# 21. Naive Bayes Customer Churn Example

Suppose dataset:

```text
Age    Tenure    MonthlyCharges    Churn
------------------------------------------------
25       2            80             1
40      36            50             0
30      12            70             1
55      48            40             0
```

Numerical features:

```text
Age
Tenure
MonthlyCharges
```

For this type of numerical data, **GaussianNB** is a natural Naive Bayes choice.

```python
from sklearn.naive_bayes import GaussianNB

model = GaussianNB()

model.fit(X_train, y_train)

prediction = model.predict(X_test)

print(prediction)
```

---

# 22. SVM vs Naive Bayes

| Feature              | SVM                            | Naive Bayes                      |
| -------------------- | ------------------------------ | -------------------------------- |
| Main idea            | Decision boundary              | Probability                      |
| Type                 | Discriminative                 | Generative/probabilistic         |
| Important concept    | Margin                         | Bayes theorem                    |
| Important parameters | C, Kernel, Gamma               | Distribution/model variant       |
| Support vectors      | Yes                            | No                               |
| Scaling              | Usually important              | Usually not required in same way |
| Non-linear data      | Kernel support                 | No kernel                        |
| Training             | Can be computationally heavier | Very fast                        |
| Text classification  | Good                           | Often excellent                  |
| Small datasets       | Can work well                  | Often works well                 |

---

# 23. SVM + Naive Bayes for Customer Churn

Typical dataset:

```text
Age
Tenure
MonthlyCharges
TotalCharges
Contract
PaymentMethod
InternetService
SeniorCitizen
...
Churn
```

Pipeline:

```text
Dataset
   ↓
EDA
   ↓
Missing Values
   ↓
Duplicate Check
   ↓
Encoding
   ↓
Train/Test Split
   ↓
Feature Scaling
   ↓
       ┌───────────────┐
       ↓               ↓
      SVM          Naive Bayes
       ↓               ↓
 Linear / RBF      GaussianNB
       ↓               ↓
       └───────┬───────┘
               ↓
        Model Evaluation
               ↓
 Accuracy / Precision
 Recall / F1 / ROC-AUC
```

---

# 24. Important SVM Interview Questions

## Q1. What is SVM?

SVM is a supervised learning algorithm that finds an optimal decision boundary with maximum margin between classes.

---

## Q2. What is a hyperplane?

Hyperplane is the decision boundary used to separate classes.

---

## Q3. What are support vectors?

The data points closest to the decision boundary are called support vectors.

---

## Q4. What is margin?

Margin is the distance between the decision boundary and the nearest support vectors.

---

## Q5. What is the goal of SVM?

> Maximize the margin between classes.

---

## Q6. What is C?

`C` controls the penalty for classification errors.

```text
High C → Strong penalty → Smaller margin
Low C  → Lower penalty  → Larger margin
```

---

## Q7. What is Kernel?

Kernel helps SVM handle non-linear decision boundaries.

---

## Q8. What is Gamma?

Gamma controls the influence/reach of individual training points, especially with the RBF kernel.

```text
Low Gamma  → Smoother boundary
High Gamma → More complex boundary
```

---

## Q9. Why is feature scaling important for SVM?

Because SVM uses distances/margins and features with larger scales can dominate the model.

---

# 25. Important Naive Bayes Interview Questions

## Q1. What is Naive Bayes?

A probabilistic classifier based on Bayes theorem and conditional independence assumption.

---

## Q2. Why is it called Naive?

Because it assumes features are conditionally independent given the class.

---

## Q3. What is Bayes theorem?

```text
P(A|B) = P(B|A) * P(A) / P(B)
```

---

## Q4. When do we use GaussianNB?

For continuous numerical features.

---

## Q5. When do we use MultinomialNB?

For count/frequency data, especially text classification.

---

## Q6. When do we use BernoulliNB?

For binary features such as 0/1 or Yes/No.

---

# 26. Master Memory Tricks

## SVM

```text
H → S → M → K → C → G
```

### H = Hyperplane

> Decision boundary

### S = Support Vector

> Boundary ke nearest points

### M = Margin

> Boundary aur support vectors ka distance

### K = Kernel

> Non-linear boundary

### C = Cost

> Mistake ki penalty

### G = Gamma

> Point ka reach/influence

---

# 27. Naive Bayes Master Trick

```text
Bayes
   ↓
Probability
   ↓
Independence
   ↓
G / M / B
```

### G = Gaussian

> Numbers

### M = Multinomial

> Counts

### B = Bernoulli

> Binary

---

# 28. Ultra Short Revision

```text
SVM
────────────────────────────
Hyperplane = Boundary
Support Vector = Nearest Point
Margin = Distance
Kernel = Non-linear
C = Mistake Cost
Gamma = Point Reach


Naive Bayes
────────────────────────────
Bayes = Probability
Naive = Independence
Gaussian = Continuous Numbers
Multinomial = Counts
Bernoulli = Binary
```

## One-Line Revision

> **SVM maximum-margin decision boundary banata hai; Support Vectors boundary ke nearest points hote hain; Kernel non-linear boundary handle karta hai; C mistake ki penalty aur Gamma point ka influence control karta hai. Naive Bayes Bayes theorem aur conditional independence par based hai, jisme Gaussian numerical data, Multinomial count data aur Bernoulli binary data ke liye use hota hai.**
