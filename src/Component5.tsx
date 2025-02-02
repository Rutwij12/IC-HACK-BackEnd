function TrigRatiosExplainer() {
  const styles = {
    container: {
      fontFamily: 'Arial, sans-serif',
      maxWidth: '800px',
      margin: '20px auto',
      padding: '20px',
      color: '#D35400'
    },
    title: {
      fontSize: '32px',
      color: '#E67E22',
      marginBottom: '24px'
    },
    section: {
      marginBottom: '20px'
    },
    sectionTitle: {
      fontSize: '24px',
      color: '#F39C12',
      marginBottom: '12px'
    },
    text: {
      fontSize: '16px',
      lineHeight: '1.6',
      color: '#E67E22'
    },
    mnemonic: {
      fontStyle: 'italic',
      color: '#F39C12',
      marginTop: '8px'
    }
  }

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>Understanding Trigonometric Ratios</h1>
      
      <div style={styles.section}>
        <h2 style={styles.sectionTitle}>Sine (sin)</h2>
        <p style={styles.text}>
          Sine is the ratio of the opposite side to the hypotenuse in a right triangle.
        </p>
        <p style={styles.mnemonic}>
          Remember: "SOH" - Sine equals Opposite over Hypotenuse
        </p>
      </div>

      <div style={styles.section}>
        <h2 style={styles.sectionTitle}>Cosine (cos)</h2>
        <p style={styles.text}>
          Cosine is the ratio of the adjacent side to the hypotenuse in a right triangle.
        </p>
        <p style={styles.mnemonic}>
          Remember: "CAH" - Cosine equals Adjacent over Hypotenuse
        </p>
      </div>

      <div style={styles.section}>
        <h2 style={styles.sectionTitle}>Tangent (tan)</h2>
        <p style={styles.text}>
          Tangent is the ratio of the opposite side to the adjacent side in a right triangle.
        </p>
        <p style={styles.mnemonic}>
          Remember: "TOA" - Tangent equals Opposite over Adjacent
        </p>
      </div>

      <div style={styles.section}>
        <h2 style={styles.sectionTitle}>SOHCAHTOA</h2>
        <p style={styles.text}>
          Put it all together and you get SOHCAHTOA - the classic mnemonic device for remembering all three ratios:
        </p>
        <p style={styles.mnemonic}>
          SOH - Sine = Opposite / Hypotenuse
          CAH - Cosine = Adjacent / Hypotenuse
          TOA - Tangent = Opposite / Adjacent
        </p>
      </div>
    </div>
  )
}