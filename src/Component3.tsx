function SetNotationGuide() {
  const styles = {
    container: {
      fontFamily: 'Arial, sans-serif',
      maxWidth: '800px',
      margin: '20px auto',
      padding: '20px',
      color: '#cc7000'
    },
    title: {
      fontSize: '28px',
      color: '#ff8c00',
      marginBottom: '20px'
    },
    section: {
      marginBottom: '24px'
    },
    sectionTitle: {
      fontSize: '20px',
      color: '#e67300',
      marginBottom: '12px'
    },
    text: {
      fontSize: '16px',
      lineHeight: '1.6',
      marginBottom: '12px'
    },
    example: {
      fontStyle: 'italic',
      color: '#ff9933',
      marginLeft: '20px'
    }
  }

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>Set Notation Guide</h1>

      <div style={styles.section}>
        <h2 style={styles.sectionTitle}>Set Definition</h2>
        <p style={styles.text}>
          A set is denoted by curly braces {} containing its elements, separated by commas.
        </p>
        <p style={styles.example}>Example: {"{1, 2, 3}"} is a set containing three numbers</p>
      </div>

      <div style={styles.section}>
        <h2 style={styles.sectionTitle}>Set Membership</h2>
        <p style={styles.text}>
          The symbol ∈ means "is an element of" and ∉ means "is not an element of"
        </p>
        <p style={styles.example}>Example: x ∈ A means x is an element of set A</p>
      </div>

      <div style={styles.section}>
        <h2 style={styles.sectionTitle}>Common Sets</h2>
        <p style={styles.text}>
          ℕ represents Natural Numbers
          ℤ represents Integers
          ℚ represents Rational Numbers
          ℝ represents Real Numbers
        </p>
      </div>

      <div style={styles.section}>
        <h2 style={styles.sectionTitle}>Set Operations</h2>
        <p style={styles.text}>
          ∪ represents Union: combines elements from both sets
          ∩ represents Intersection: elements common to both sets
          \ represents Set Difference: elements in first set but not in second
        </p>
        <p style={styles.example}>Example: A ∪ B contains all elements from both A and B</p>
      </div>

      <div style={styles.section}>
        <h2 style={styles.sectionTitle}>Set Properties</h2>
        <p style={styles.text}>
          ⊆ means "is a subset of"
          ⊂ means "is a proper subset of"
          = means sets contain exactly the same elements
        </p>
        <p style={styles.example}>Example: If A ⊆ B, all elements of A are also in B</p>
      </div>

      <div style={styles.section}>
        <h2 style={styles.sectionTitle}>Special Sets</h2>
        <p style={styles.text}>
          ∅ or {} represents the Empty Set
          U represents the Universal Set
        </p>
        <p style={styles.example}>Example: The empty set ∅ contains no elements</p>
      </div>
    </div>
  )
}