function MatrixBasicsText() {
  const styles = {
    container: {
      fontFamily: 'Arial, sans-serif',
      maxWidth: '800px',
      margin: '20px auto',
      padding: '20px',
      color: '#1a365d'
    },
    title: {
      fontSize: '28px',
      color: '#2c5282',
      marginBottom: '20px'
    },
    subtitle: {
      fontSize: '22px',
      color: '#2b6cb0',
      marginTop: '20px',
      marginBottom: '12px'
    },
    paragraph: {
      fontSize: '16px',
      lineHeight: '1.6',
      marginBottom: '16px',
      color: '#2d3748'
    }
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>Understanding Matrix Multiplication</h1>

      <h2 style={styles.subtitle}>What is Matrix Multiplication?</h2>
      <p style={styles.paragraph}>
        Matrix multiplication is an operation that combines two matrices to create a new matrix. 
        Unlike regular multiplication, matrix multiplication involves a specific process of multiplying 
        and adding elements in a particular pattern.
      </p>

      <h2 style={styles.subtitle}>Basic Rules</h2>
      <p style={styles.paragraph}>
        To multiply two matrices, the number of columns in the first matrix must equal the number 
        of rows in the second matrix. The resulting matrix will have the same number of rows as 
        the first matrix and the same number of columns as the second matrix.
      </p>

      <h2 style={styles.subtitle}>The Process</h2>
      <p style={styles.paragraph}>
        Each element in the resulting matrix is calculated by taking a row from the first matrix 
        and a column from the second matrix. We multiply corresponding elements and add the products. 
        This process is repeated for each position in the resulting matrix.
      </p>

      <h2 style={styles.subtitle}>Key Properties</h2>
      <p style={styles.paragraph}>
        Matrix multiplication is not commutative, meaning A × B is not necessarily equal to B × A. 
        However, it is associative, meaning (A × B) × C equals A × (B × C). The identity matrix, 
        when multiplied with any matrix, returns the original matrix.
      </p>

      <h2 style={styles.subtitle}>Applications</h2>
      <p style={styles.paragraph}>
        Matrix multiplication is fundamental in many fields including computer graphics for transformations, 
        quantum mechanics for state changes, and machine learning for data transformations. It's also 
        essential in solving systems of linear equations and in various optimization problems.
      </p>
    </div>
  );
}