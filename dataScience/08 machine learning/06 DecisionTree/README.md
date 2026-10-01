# Decision Tree + Random Forest --- Step-by-Step Notes
<!-------------------------------------------------------------- 

Decision Tree basics
Entropy + formula + example
Gini Impurity + formula + example
Information Gain
Tree depth
Overfitting / Underfitting
Pre-pruning / Post-pruning
Bagging
Bootstrap sampling
Random Forest
Random feature selection
Feature importance
Decision Tree vs Random Forest
Python scikit-learn examples
Life-based examples: customer purchase, loan approval, movie analysis
Interview questions
Final revision cheat sheet

------------------------------------------------------------------->



## 1. What is a Decision Tree?

A **Decision Tree** is a machine learning algorithm that makes decisions
by asking a sequence of questions.

Think of it like a person making a decision:

> "Should I carry an umbrella today?"

The person may ask:

1.  Is it raining?
2.  If yes → carry an umbrella.
3.  If no → is the sky cloudy?
4.  If cloudy → maybe carry an umbrella.
5.  Otherwise → don't carry it.

A Decision Tree works in a similar way with data.

### Simple real-life example

Suppose we want to predict:

**Will a customer buy a product?**

  Income     Website Visits Previous Purchase   Buy
  -------- ---------------- ------------------- -----
  High                   10 Yes                 Yes
  High                    8 Yes                 Yes
  Low                     2 No                  No
  Low                     3 No                  No
  Medium                  7 Yes                 Yes

The tree may learn:

``` text

Previous Purchase?
       |
   +---+---+
  Yes      No
   |        |
  BUY    DON'T BUY

```

The tree keeps splitting the data until it can make useful predictions.

------------------------------------------------------------------------

# 2. Important Terms

Before understanding Decision Trees, learn these terms:

### Root Node

The first question/split in the tree.

Example:

``` text
Income > 50000?
```

### Internal Node

A question inside the tree.

Example:

``` text
Previous Purchase = Yes?
```

### Branch

The result of a question.

Example:

``` text
Yes
No
```

### Leaf Node

The final prediction.

Example:

``` text
BUY
DON'T BUY
```

### Depth

How many levels the tree has.

Example:

``` text
                 Income?
                /       \
              High      Low
               |         |
           Purchase?    DON'T BUY
            /    \
          Yes     No
          |       |
         BUY   DON'T BUY
```

This tree has depth around 2 from the root.

------------------------------------------------------------------------

# 3. Why Does a Tree Need to Split Data?

Suppose we have:

``` text
YES YES YES NO NO NO
```

This group contains two classes.

It is **impure**.

If we split it into:

``` text
Group 1 → YES YES YES

Group 2 → NO NO NO
```

each group becomes pure.

A Decision Tree tries to find splits that make the resulting groups as
pure as possible.

This is where:

-   Entropy
-   Gini Impurity
-   Information Gain

become important.

------------------------------------------------------------------------

# 4. Entropy

## What is Entropy?

**Entropy measures impurity or uncertainty in data.**

Simple idea:

> More mixed classes = higher entropy\
> One class only = lower entropy

### Real-life example

Imagine two boxes of balls.

### Box A

``` text
RED RED RED RED
```

There is no uncertainty.

Entropy = **0**

### Box B

``` text
RED BLUE RED BLUE
```

We don't know what color we will get.

Entropy is higher.

------------------------------------------------------------------------

# 5. Entropy Formula

For classification:

``` text
Entropy = - Σ p(x) log2(p(x))
```

Where:

-   `p(x)` = probability of a class
-   `Σ` = sum
-   `log2` = logarithm base 2

For two classes:

``` text
Entropy = -p(Yes)log2(p(Yes))
          -p(No)log2(p(No))
```

------------------------------------------------------------------------

# 6. Entropy Example

Suppose 10 customers are:

``` text
6 BUY
4 DON'T BUY
```

Then:

``` text
P(BUY) = 6/10 = 0.6

P(DON'T BUY) = 4/10 = 0.4
```

Entropy:

``` text
Entropy =
-(0.6 × log2(0.6))
-(0.4 × log2(0.4))
```

Approximately:

``` text
Entropy ≈ 0.971
```

This means the group has significant uncertainty.

------------------------------------------------------------------------

# 7. Pure vs Impure Data

### Completely Pure

``` text
BUY
BUY
BUY
BUY
```

Entropy:

``` text
0
```

### Completely Mixed

For two classes with a 50/50 split:

``` text
BUY
DON'T BUY
BUY
DON'T BUY
```

Entropy:

``` text
1
```

For binary classification:

``` text
Entropy range = 0 to 1
```

Generally:

``` text
0       → completely pure
1       → maximum uncertainty
```

------------------------------------------------------------------------

# 8. Gini Impurity

Another method used by Decision Trees is **Gini Impurity**.

Gini also measures how mixed the classes are.

Simple idea:

> Lower Gini = better/purer node.

### Formula

``` text
Gini = 1 - Σ p(x)^2
```

For two classes:

``` text
Gini = 1 - [P(Yes)^2 + P(No)^2]
```

------------------------------------------------------------------------

# 9. Gini Example

Suppose:

``` text
6 BUY
4 DON'T BUY
```

Then:

``` text
P(BUY) = 0.6
P(DON'T BUY) = 0.4
```

Therefore:

``` text
Gini = 1 - (0.6² + 0.4²)

     = 1 - (0.36 + 0.16)

     = 1 - 0.52

     = 0.48
```

So:

``` text
Gini = 0.48
```

------------------------------------------------------------------------

# 10. Entropy vs Gini

  Concept                             Entropy            Gini
  ----------------------------------- ------------------ ----------------------
  Measures                            Uncertainty        Impurity
  Best value                          0                  0
  Maximum for binary classification   1                  0.5
  Formula                             `-Σp log2(p)`      `1 - Σp²`
  Common use                          Information Gain   Gini-based splitting

In practice, both can produce similar trees.

In `scikit-learn`, Decision Trees commonly use:

``` python
criterion="gini"
```

or:

``` python
criterion="entropy"
```

------------------------------------------------------------------------

# 11. Information Gain

Now we need to answer:

> Which feature should the tree use for splitting?

This is where **Information Gain** is used.

Information Gain tells us how much uncertainty is reduced after a split.

### Basic idea

``` text
Information Gain
=
Parent Entropy
-
Weighted Child Entropy
```

Higher Information Gain generally means a better split.

------------------------------------------------------------------------

# 12. Information Gain --- Life Example

Suppose a shop has 10 customers:

``` text
6 BUY
4 DON'T BUY
```

Parent entropy:

``` text
0.971
```

Now split customers based on:

``` text
Previous Purchase?
```

Suppose:

``` text
Previous Purchase = YES
5 customers → 5 BUY

Previous Purchase = NO
5 customers → 1 BUY, 4 DON'T BUY
```

The first group is completely pure.

The second group is mostly `DON'T BUY`.

The weighted child entropy becomes lower than the parent entropy.

Therefore:

``` text
Information Gain > 0
```

The split was useful.

------------------------------------------------------------------------

# 13. How a Decision Tree Chooses a Split

Suppose we have features:

``` text
Age
Income
Previous Purchase
Website Visits
```

The tree tests possible splits.

Example:

``` text
Age > 30?
Income > 50000?
Previous Purchase = Yes?
Website Visits > 5?
```

For every possible split it calculates impurity/information gain.

Then it chooses a useful split.

Conceptually:

``` text
Calculate possible splits
          ↓
Measure impurity
          ↓
Calculate Information Gain / impurity reduction
          ↓
Choose useful split
          ↓
Repeat for child nodes
```

------------------------------------------------------------------------

# 14. Decision Tree Example

Imagine an online store.

Goal:

``` text
Predict whether customer will BUY.
```

Features:

``` text
Age
Income
Website Visits
Previous Purchase
```

The tree might become:

``` text
                Previous Purchase?
                  /            \
                Yes             No
                /                \
              BUY            Website Visits?
                              /          \
                           > 5            <= 5
                            |               |
                           BUY          DON'T BUY
```

This is easy for humans to understand.

------------------------------------------------------------------------

# 15. What is Tree Depth?

**Tree depth** tells us how many levels the tree can grow.

Example:

``` text
Depth 1

       Income?
       /     \
     Yes     No
```

Depth 2:

``` text
       Income?
       /     \
     Yes     No
             |
         Visits?
```

Depth 3:

``` text
       Income?
       /     \
     Yes     No
             |
          Visits?
          /    \
        High   Low
                |
            Purchase?
```

------------------------------------------------------------------------

# 16. Why Tree Depth Matters

A very deep tree can memorize training data.

This is called:

## Overfitting

Example:

``` text
Training accuracy = 100%
Testing accuracy = 70%
```

The model may have learned the training examples too specifically.

A shallow tree may be too simple.

This is called:

## Underfitting

Example:

``` text
Training accuracy = 70%
Testing accuracy = 68%
```

The model has not learned enough patterns.

------------------------------------------------------------------------

# 17. Controlling Tree Depth

In `scikit-learn`:

``` python
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(
    max_depth=5,
    random_state=42
)
```

Important parameter:

``` text
max_depth
```

It limits how deep the tree can grow.

Other useful parameters:

``` python
min_samples_split
min_samples_leaf
max_leaf_nodes
```

------------------------------------------------------------------------

# 18. Pruning

## What is Pruning?

Pruning means:

> Removing unnecessary branches from a Decision Tree.

Think about a real-life decision process.

Bad decision process:

``` text
Is customer age > 27?
   |
Does customer live in Zone A?
   |
Is customer name length > 6?
   |
Did customer visit website at 10:35 AM?
   |
BUY?
```

This may be too complicated.

A simpler tree may be:

``` text
Previous Purchase?
      /       \
    Yes        No
    |           |
   BUY      DON'T BUY
```

The simpler tree may generalize better to new customers.

------------------------------------------------------------------------

# 19. Pre-Pruning vs Post-Pruning

### Pre-Pruning

Stop the tree from growing too much.

Examples:

``` python
max_depth=5
min_samples_split=10
min_samples_leaf=5
```

### Post-Pruning

First grow a larger tree, then remove unnecessary branches.

In `scikit-learn`, cost-complexity pruning can be controlled using:

``` python
ccp_alpha
```

Example:

``` python
model = DecisionTreeClassifier(
    ccp_alpha=0.01,
    random_state=42
)
```

Higher pruning strength can produce a simpler tree.

------------------------------------------------------------------------

# 20. Decision Tree Advantages

### Advantages

-   Easy to understand
-   Easy to visualize
-   Works with nonlinear relationships
-   Little feature scaling required
-   Can handle numerical and categorical data after suitable
    preprocessing
-   Useful for explaining decisions

### Disadvantages

-   Can overfit
-   Small data changes can produce a different tree
-   A single tree may have lower generalization performance than an
    ensemble
-   Very deep trees become difficult to interpret

------------------------------------------------------------------------

# 21. What is Random Forest?

A **Random Forest** is an ensemble of many Decision Trees.

Instead of asking:

> "What does one tree say?"

we ask:

> "What do many trees say?"

For classification, the trees generally vote.

Example:

``` text
Tree 1 → BUY
Tree 2 → BUY
Tree 3 → DON'T BUY
Tree 4 → BUY
Tree 5 → BUY

Final Prediction → BUY
```

------------------------------------------------------------------------

# 22. Why Do We Need Many Trees?

A single Decision Tree can be unstable.

Example:

``` text
Small change in training data
            ↓
Different split
            ↓
Different branches
            ↓
Different prediction
```

Random Forest reduces this instability by combining many trees.

------------------------------------------------------------------------

# 23. Bagging

Random Forest uses an important idea called:

## Bagging

Bagging = **Bootstrap Aggregating**

The basic process:

``` text
Original Dataset
       ↓
Create many bootstrap datasets
       ↓
Train one Decision Tree on each dataset
       ↓
Combine predictions
       ↓
Final Prediction
```

------------------------------------------------------------------------

# 24. What is Bootstrap Sampling?

Bootstrap sampling means:

> Randomly select samples from the dataset **with replacement**.

Suppose our original dataset is:

``` text
A B C D E
```

A bootstrap sample might be:

``` text
A C C E B
```

Notice:

``` text
C appears twice
D is missing
```

This is allowed because sampling is done **with replacement**.

Another bootstrap sample might be:

``` text
B B D E A
```

------------------------------------------------------------------------

# 25. Why Bootstrap Helps

Each tree sees a slightly different dataset.

Therefore:

``` text
Tree 1 → Dataset A
Tree 2 → Dataset B
Tree 3 → Dataset C
Tree 4 → Dataset D
...
```

The trees become different from each other.

Combining their predictions can reduce variance and improve
generalization.

------------------------------------------------------------------------

# 26. Random Feature Selection

Random Forest does not only randomize rows.

It can also randomly consider a subset of features when finding splits.

Example:

Original features:

``` text
Age
Income
Education
Website Visits
Previous Purchase
Location
```

One tree may consider:

``` text
Age
Income
Previous Purchase
```

Another tree may consider:

``` text
Education
Website Visits
Location
```

This adds more diversity among trees.

------------------------------------------------------------------------

# 27. Random Forest Complete Flow

``` text
                    Original Dataset
                           |
              +------------+------------+
              |            |            |
              ↓            ↓            ↓
        Bootstrap 1   Bootstrap 2   Bootstrap 3
              |            |            |
              ↓            ↓            ↓
           Tree 1        Tree 2       Tree 3
              |            |            |
              +------------+------------+
                           |
                     Combine Results
                           |
                           ↓
                    Final Prediction
```

------------------------------------------------------------------------

# 28. Random Forest Classification

Suppose there are 5 trees:

``` text
Tree 1 → Spam
Tree 2 → Not Spam
Tree 3 → Spam
Tree 4 → Spam
Tree 5 → Not Spam
```

Voting:

``` text
Spam = 3
Not Spam = 2
```

Final prediction:

``` text
SPAM
```

This is called **majority voting**.

------------------------------------------------------------------------

# 29. Random Forest Regression

Random Forest can also solve regression problems.

Suppose five trees predict house prices:

``` text
Tree 1 → ₹50 lakh
Tree 2 → ₹52 lakh
Tree 3 → ₹49 lakh
Tree 4 → ₹51 lakh
Tree 5 → ₹53 lakh
```

The final prediction can be based on the average:

``` text
(50 + 52 + 49 + 51 + 53) / 5
= ₹51 lakh
```

------------------------------------------------------------------------

# 30. Decision Tree vs Random Forest

  Feature                 Decision Tree    Random Forest
  ----------------------- ---------------- ------------------
  Number of trees         One              Many
  Bagging                 No               Yes
  Bootstrap samples       No               Yes
  Stability               Lower            Generally higher
  Overfitting risk        Higher if deep   Often lower
  Interpretability        High             Lower
  Training complexity     Lower            Higher
  Prediction complexity   Lower            Higher
  Feature importance      Yes              Yes

------------------------------------------------------------------------

# 31. Feature Importance

Feature importance answers:

> Which features contributed most to the model's decisions?

Suppose we predict customer purchase:

``` text
Age
Income
Website Visits
Previous Purchase
```

The model may report:

``` text
Previous Purchase → 0.45
Website Visits    → 0.30
Income            → 0.20
Age               → 0.05
```

This tells us the model relied more heavily on `Previous Purchase` than
the other features under the model's importance calculation.

Important:

> Feature importance is about the model's behavior. It does not
> automatically prove that a feature causes the outcome.

------------------------------------------------------------------------

# 32. Feature Importance in Python

``` python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

importance = model.feature_importances_

for feature, score in zip(X_train.columns, importance):
    print(feature, score)
```

Example output:

``` text
Age                 0.08
Income              0.21
Website Visits      0.26
Previous Purchase   0.45
```

------------------------------------------------------------------------

# 33. Important Random Forest Parameters

### n_estimators

Number of trees.

``` python
RandomForestClassifier(
    n_estimators=100
)
```

Example:

``` text
100 → 100 trees
500 → 500 trees
```

More trees can improve stability, but increase computation.

------------------------------------------------------------------------

### max_depth

Maximum depth of each tree.

``` python
RandomForestClassifier(
    n_estimators=100,
    max_depth=10
)
```

------------------------------------------------------------------------

### min_samples_split

Minimum number of samples required to split a node.

``` python
min_samples_split=10
```

------------------------------------------------------------------------

### min_samples_leaf

Minimum number of samples required in a leaf.

``` python
min_samples_leaf=5
```

------------------------------------------------------------------------

### max_features

Number/proportion of features considered when looking for a split.

Example:

``` python
max_features="sqrt"
```

------------------------------------------------------------------------

### bootstrap

Whether bootstrap samples are used.

``` python
bootstrap=True
```

------------------------------------------------------------------------

# 34. Complete Random Forest Example

## Problem

Predict whether a customer will purchase a product.

Features:

``` text
Age
Income
Website Visits
Previous Purchase
```

Target:

``` text
Buy
```

### Python

``` python
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load data
df = pd.read_csv("customers.csv")

# Features
X = df[
    [
        "Age",
        "Income",
        "WebsiteVisits",
        "PreviousPurchase"
    ]
]

# Target
y = df["Buy"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Create model
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))

print(classification_report(y_test, y_pred))
```

------------------------------------------------------------------------

# 35. Decision Tree Python Example

``` python
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=5,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
```

Using Entropy:

``` python
model = DecisionTreeClassifier(
    criterion="entropy",
    max_depth=5,
    random_state=42
)
```

------------------------------------------------------------------------

# 36. Visualizing a Decision Tree

``` python
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(20, 10))

plot_tree(
    model,
    feature_names=X.columns,
    class_names=["No", "Yes"],
    filled=True
)

plt.show()
```

This helps us see:

``` text
Root
 ↓
Question
 ↓
Branch
 ↓
Question
 ↓
Leaf / Prediction
```

------------------------------------------------------------------------

# 37. Practical Life Example --- Loan Approval

Imagine a bank wants to predict whether a loan applicant is likely to
repay.

Features:

``` text
Income
Credit Score
Age
Existing Loans
Employment Years
```

A Decision Tree might reason:

``` text
Credit Score > 700?
       |
   +---+---+
  Yes      No
   |        |
Income?   Reject
 /   \
High Low
 |    |
Approve  Review
```

Random Forest creates many such trees and combines their predictions.

------------------------------------------------------------------------

# 38. Practical Life Example --- Movie Recommendation / Rating

Suppose we want to analyze whether a movie may receive a high rating.

Features might include:

``` text
Genre
Budget
Runtime
Number of Votes
Release Year
Lead Actor Popularity
Director
```

A tree might find:

``` text
Number of Votes > 10000?
        |
     +--+--+
    Yes     No
     |       |
Budget?    Lower confidence
```

A Random Forest can combine many different trees to capture more complex
patterns.

------------------------------------------------------------------------

# 39. Easy Mental Model

Remember the whole topic like this:

``` text
Decision Tree
     ↓
Ask questions
     ↓
Split data
     ↓
Measure impurity
     ↓
Choose best split
     ↓
Repeat
     ↓
Prediction
```

Random Forest:

``` text
Many Decision Trees
        ↓
Bootstrap samples
        ↓
Random feature subsets
        ↓
Train many trees
        ↓
Voting / Averaging
        ↓
Final Prediction
```

------------------------------------------------------------------------

# 40. One-Line Meaning of Every Important Term

  Term                 Easy Meaning
  -------------------- ----------------------------------------------------
  Decision Tree        One tree making decisions
  Root                 First question
  Node                 Decision/question point
  Branch               Answer to a question
  Leaf                 Final prediction
  Tree Depth           Number of levels
  Entropy              Measures uncertainty
  Gini                 Measures impurity
  Information Gain     Measures reduction in uncertainty
  Pruning              Removing unnecessary branches
  Overfitting          Model memorizes training data
  Bagging              Train models on bootstrap samples and combine them
  Bootstrap            Random sampling with replacement
  Random Forest        Many Decision Trees combined
  n_estimators         Number of trees
  Feature Importance   How much the model used each feature

------------------------------------------------------------------------

# 41. Interview Questions

## Q1. What is a Decision Tree?

A Decision Tree is a supervised learning algorithm that recursively
splits data using feature-based rules to make predictions.

## Q2. What is Entropy?

Entropy measures the uncertainty or impurity of a node.

``` text
Entropy = -Σ p log2(p)
```

## Q3. What is Gini Impurity?

Gini measures the probability of incorrect classification if a label is
randomly assigned according to the class distribution.

``` text
Gini = 1 - Σp²
```

## Q4. What is Information Gain?

Information Gain measures how much entropy is reduced after a split.

``` text
Information Gain
=
Parent Entropy
-
Weighted Child Entropy
```

## Q5. What is pruning?

Pruning removes unnecessary branches to reduce model complexity and
overfitting.

## Q6. What is tree depth?

Tree depth is the number of levels from the root to the deepest leaf.

## Q7. What is Bagging?

Bagging means training multiple models using bootstrap samples and
aggregating their predictions.

## Q8. What is Bootstrap Sampling?

Sampling randomly **with replacement** from the original dataset.

## Q9. What is Random Forest?

Random Forest is an ensemble of Decision Trees that uses bootstrap
samples and random feature selection, then combines tree predictions.

## Q10. Why is Random Forest generally more stable than one Decision Tree?

Because it combines predictions from many diverse trees, which can
reduce the effect of an individual tree's variance.

## Q11. What is feature importance?


It is a model-derived measure indicating how much each feature
contributes to the model's splitting/prediction process.

------------------------------------------------------------------------

# 42. Final Revision Cheat Sheet

``` text
                    DECISION TREE
                         |
             +-----------+-----------+
             |                       |
          Entropy                  Gini
             |                       |
       Uncertainty                 Impurity
             \                       /
              \                     /
               Information Gain
                       |
                 Best Split
                       |
                  Tree Depth
                       |
                    Pruning
                       |
                  Final Tree
```


``` text
                  RANDOM FOREST
                        |
              Many Decision Trees
                        |
                 Bootstrap Data
                        |
               Random Features
                        |
                   Bagging
                        |
              Combine Predictions
                        |
                Final Prediction
                        |
               Feature Importance
```

------------------------------------------------------------------------

# 43. What You Should Remember for ML Interviews

The most important flow is:

``` text
Decision Tree
→ split data
→ calculate Gini/Entropy
→ choose best split
→ repeat
→ control depth
→ prune if needed
→ predict
```

And:

``` text
Random Forest
→ create bootstrap samples
→ train many Decision Trees
→ use random feature subsets
→ combine predictions
→ reduce variance
→ calculate feature importance
```

### Golden Rule

> **Decision Tree = one decision-making tree**

> **Random Forest = many different decision trees working together**

> **Entropy/Gini = how impure is the data?**

> **Information Gain = how useful is this split?**

> **Pruning/Depth = how complex should the tree be?**

> **Bagging/Bootstrap = how do we create diverse training sets for many
> trees?**

> **Feature Importance = which features did the model rely on most?**
