Certainly! Below, I'll provide both solutions in Markdown format, covering both the matrix method and the substitution method for solving the system of linear equations:

### Solution Using Matrix Algebra

#### Step-by-Step Solution:

1. **Define vectors and matrices:**
   - \(\mathbf{x} = \begin{bmatrix} a \\ b \end{bmatrix}\)
   - \(\mathbf{p} = \begin{bmatrix} p_0 \\ p_1 \end{bmatrix}\)
   - Matrix \(A = \begin{bmatrix} a_0 & b_0 \\ a_1 & b_1 \end{bmatrix}\)

2. **Write the system as a matrix equation:**
   \[
   A \mathbf{x} = \mathbf{p}
   \]

3. **Calculate the determinant of \(A\):**
   \[
   \text{det}(A) = a_0 b_1 - b_0 a_1
   \]

4. **Find the inverse of \(A\) (if \(\text{det}(A) \neq 0\)):**
   \[
   A^{-1} = \frac{1}{\text{det}(A)} \begin{bmatrix} b_1 & -b_0 \\ -a_1 & a_0 \end{bmatrix}
   \]

5. **Multiply \(A^{-1}\) by \(\mathbf{p}\) to solve for \(\mathbf{x}\):**
   \[
   \mathbf{x} = A^{-1} \mathbf{p} = \frac{1}{\text{det}(A)} \begin{bmatrix} b_1 & -b_0 \\ -a_1 & a_0 \end{bmatrix} \begin{bmatrix} p_0 \\ p_1 \end{bmatrix}
   \]
   \[
   \mathbf{x} = \frac{1}{\text{det}(A)} \begin{bmatrix} b_1 p_0 - b_0 p_1 \\ -a_1 p_0 + a_0 p_1 \end{bmatrix}
   \]

   Solution:
   \[
   a = \frac{b_1 p_0 - b_0 p_1}{\text{det}(A)}
   \]
   \[
   b = \frac{-a_1 p_0 + a_0 p_1}{\text{det}(A)}
   \]

### Solution Using Substitution Method

#### Step-by-Step Solution:

1. **Express \(b\) from the second equation:**
   \[
   a \cdot a_1 + b \cdot b_1 = p_1 \quad \Rightarrow \quad b = \frac{p_1 - a \cdot a_1}{b_1}
   \]

2. **Substitute \(b\) in the first equation:**
   \[
   a \cdot a_0 + \left(\frac{p_1 - a \cdot a_1}{b_1}\right) \cdot b_0 = p_0
   \]
   Simplify:
   \[
   a \cdot a_0 + \frac{p_1 \cdot b_0 - a \cdot a_1 \cdot b_0}{b_1} = p_0
   \]
   Factor \(a\):
   \[
   a \cdot \left(a_0 - \frac{a_1 \cdot b_0}{b_1}\right) = p_0 - \frac{p_1 \cdot b_0}{b_1}
   \]

3. **Solve for \(a\):**
   \[
   a = \frac{b_1 \cdot p_0 - p_1 \cdot b_0}{b_1 \cdot a_0 - a_1 \cdot b_0}
   \]

This Markdown presentation helps to present each solution method clearly and methodically for solving the equations:
- \( a \cdot a_0 + b \cdot b_0 = p_0 \)
- \( a \cdot a_1 + b \cdot b_1 = p_1 \)
