function SetOperationsExplainer() {
  const styles = {
    container: {
      fontFamily: 'Arial, sans-serif',
      maxWidth: '800px',
      margin: '20px auto',
      padding: '20px',
      color: '#CC7000'
    },
    title: {
      fontSize: '28px',
      color: '#FF8C00',
      marginBottom: '20px'
    },
    section: {
      marginBottom: '24px'
    },
    sectionTitle: {
      fontSize: '20px',
      color: '#FFA500',
      marginBottom: '12px'
    },
    content: {
      fontSize: '16px',
      lineHeight: '1.6',
      color: '#E67300'
    }
  }

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>Set Operations Explained</h1>
      
      <div style={styles.section}>
        <h2 style={styles.sectionTitle}>Union</h2>
        <p style={styles.content}>
          The union of two sets A and B is the set that contains all elements from both A and B, with duplicates removed. 
          It represents combining all unique elements from both sets into a single set. The union is denoted as A ∪ B.
        </p>
      </div>

      <div style={styles.section}>
        <h2 style={styles.sectionTitle}>Intersection</h2>
        <p style={styles.content}>
          The intersection of two sets A and B is the set containing only the elements that appear in both A and B.
          It represents the common elements between two sets. The intersection is denoted as A ∩ B.
        </p>
      </div>

      <div style={styles.section}>
        <h2 style={styles.sectionTitle}>Complement</h2>
        <p style={styles.content}>
          The complement of a set A is all elements in the universal set that are not in A.
          It represents everything that is not included in the original set. The complement is denoted as A' or A^c.
        </p>
      </div>

      <div style={styles.section}>
        <h2 style={styles.sectionTitle}>Difference</h2>
        <p style={styles.content}>
          The difference between sets A and B (A - B) is the set of elements that are in A but not in B.
          It represents what remains in the first set after removing elements that appear in the second set.
        </p>
      </div>
    </div>
  )
}