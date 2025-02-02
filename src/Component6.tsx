function BasicMathNotationGuide() {
  return (
    <div style={{ 
      fontFamily: 'Arial, sans-serif',
      color: '#D35400',
      padding: '20px',
      maxWidth: '800px'
    }}>
      <h1 style={{ 
        fontSize: '28px',
        color: '#E67E22',
        marginBottom: '20px'
      }}>
        Basic Guide to Eigenvector Notation
      </h1>

      <div style={{ marginBottom: '24px' }}>
        <h2 style={{ 
          fontSize: '22px',
          color: '#F39C12',
          marginBottom: '12px'
        }}>
          Definition
        </h2>
        <p style={{ lineHeight: '1.6' }}>
          An eigenvector is a non-zero vector that changes only by a scalar factor when a linear transformation is applied.
        </p>
      </div>

      <div style={{ marginBottom: '24px' }}>
        <h2 style={{ 
          fontSize: '22px',
          color: '#F39C12',
          marginBottom: '12px'
        }}>
          Basic Notation
        </h2>
        <p style={{ lineHeight: '1.6' }}>
          The standard notation for eigenvectors is: Av = λv
          Where:
          - A is a square matrix
          - v is an eigenvector
          - λ (lambda) is the eigenvalue
        </p>
      </div>

      <div style={{ marginBottom: '24px' }}>
        <h2 style={{ 
          fontSize: '22px',
          color: '#F39C12',
          marginBottom: '12px'
        }}>
          Written Form
        </h2>
        <p style={{ lineHeight: '1.6' }}>
          When writing about eigenvectors, we typically say:
          "v is an eigenvector of A with eigenvalue λ"
        </p>
      </div>

      <div style={{ marginBottom: '24px' }}>
        <h2 style={{ 
          fontSize: '22px',
          color: '#F39C12',
          marginBottom: '12px'
        }}>
          Important Properties
        </h2>
        <p style={{ lineHeight: '1.6' }}>
          1. Eigenvectors can only be found for square matrices
          2. A matrix may have multiple eigenvector-eigenvalue pairs
          3. Eigenvectors corresponding to different eigenvalues are linearly independent
          4. The zero vector is never an eigenvector
        </p>
      </div>

      <div>
        <h2 style={{ 
          fontSize: '22px',
          color: '#F39C12',
          marginBottom: '12px'
        }}>
          Common Usage
        </h2>
        <p style={{ lineHeight: '1.6' }}>
          Eigenvectors are typically written in column form and are often normalized (made to have length 1).
          They are commonly used in:
          - Principal Component Analysis (PCA)
          - Diagonalization
          - Quantum Mechanics
          - Computer Graphics
        </p>
      </div>
    </div>
  );
}