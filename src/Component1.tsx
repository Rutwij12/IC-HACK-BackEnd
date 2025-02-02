function QuickIntroText() {
  return (
    <div style={{
      fontFamily: 'Arial',
      color: '#FF8533',
      padding: '20px',
      maxWidth: '800px',
      margin: '0 auto'
    }}>
      <h2 style={{
        fontSize: '28px',
        color: '#FF6600',
        marginBottom: '20px'
      }}>
        What is Integration?
      </h2>

      <div style={{
        fontSize: '18px',
        lineHeight: '1.6',
        color: '#FF944D'
      }}>
        <p>
          Integration is a fundamental concept in calculus that helps us find the total amount
          of a quantity over an interval. Think of it as adding up infinitely many infinitely
          small pieces to find a total.
        </p>

        <h3 style={{
          fontSize: '22px',
          color: '#FF751A',
          marginTop: '20px',
          marginBottom: '15px'
        }}>
          Real World Applications
        </h3>

        <p>
          We use integration in countless real-world scenarios:
        </p>

        <ul style={{color: '#FF944D', marginLeft: '20px'}}>
          <li>Calculating the total distance traveled from speed</li>
          <li>Finding the volume of irregular shapes</li>
          <li>Computing the total energy consumption over time</li>
          <li>Determining the center of mass of objects</li>
          <li>Analyzing probability distributions in statistics</li>
        </ul>

        <p style={{marginTop: '15px'}}>
          Whether you're an engineer designing buildings, a physicist studying motion,
          or an economist analyzing market trends, integration provides the tools to
          understand how quantities accumulate and change over time or space.
        </p>
      </div>
    </div>
  );
}