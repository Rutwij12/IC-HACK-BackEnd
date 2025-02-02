function SetDefinitionText() {
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
    subtitle: {
      fontSize: '22px',
      color: '#ffa500',
      marginTop: '20px',
      marginBottom: '12px'
    },
    text: {
      fontSize: '16px',
      lineHeight: '1.6',
      marginBottom: '16px'
    }
  }

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>Understanding Mathematical Sets</h1>

      <h2 style={styles.subtitle}>What is a Set?</h2>
      <p style={styles.text}>
        A set is a collection of distinct objects, considered as an object in its own right. The objects in a set are called its elements or members. Sets are usually denoted by capital letters.
      </p>

      <h2 style={styles.subtitle}>Basic Properties of Sets</h2>
      <p style={styles.text}>
        Sets have several fundamental properties:
        • Sets are unordered - the order of elements doesn't matter
        • Sets contain unique elements - no duplicates are allowed
        • Sets can be finite or infinite in size
        • Sets can contain any type of objects
      </p>

      <h2 style={styles.subtitle}>Set Notation</h2>
      <p style={styles.text}>
        Sets are typically written using curly braces. The elements inside can be listed explicitly or described using a rule or condition. A set can also be empty, containing no elements at all.
      </p>

      <h2 style={styles.subtitle}>Working with Sets</h2>
      <p style={styles.text}>
        Sets can be manipulated through various operations like union (combining sets), intersection (finding common elements), and complement (elements not in a set). These operations allow us to solve complex problems and represent relationships between different groups of objects.
      </p>
    </div>
  )
}