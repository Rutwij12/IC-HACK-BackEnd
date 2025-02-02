function RealWorldExampleCards() {
  const examples = [
    {
      field: "Architecture",
      description: "Calculating roof angles and support beam placement. Architects use trigonometry to determine optimal roof pitches for drainage and load distribution.",
      icon: "🏛️"
    },
    {
      field: "Civil Engineering", 
      description: "Bridge design and construction. Engineers use trigonometric functions to calculate cable tensions and arch supports in bridge structures.",
      icon: "🌉"
    },
    {
      field: "Aviation",
      description: "Flight navigation and control. Pilots use trigonometry to calculate flight paths, angles of ascent/descent, and wind compensation.",
      icon: "✈️"
    },
    {
      field: "Marine Navigation",
      description: "Ship routing and positioning. Navigators use trigonometric calculations to determine bearings, distances and positions at sea.",
      icon: "🚢"
    },
    {
      field: "Game Development",
      description: "Character movement and collision detection. Game developers use trig to calculate realistic object motion and interactions.",
      icon: "🎮"
    },
    {
      field: "Music",
      description: "Sound wave analysis and synthesis. Audio engineers use trigonometric functions to process and create sound waves.",
      icon: "🎵"
    }
  ];

  return (
    <div style={{
      fontFamily: 'Arial',
      padding: '20px',
      maxWidth: '1200px',
      margin: '0 auto'
    }}>
      <h2 style={{
        color: '#D35400',
        fontSize: '28px',
        marginBottom: '30px',
        textAlign: 'center'
      }}>
        Real-World Applications of Trigonometry
      </h2>
      
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
        gap: '20px',
        justifyContent: 'center'
      }}>
        {examples.map((example, index) => (
          <div key={index} style={{
            backgroundColor: '#FFF3E0',
            padding: '20px',
            borderRadius: '8px',
            boxShadow: '0 2px 4px rgba(0,0,0,0.1)',
            transition: 'transform 0.2s',
            cursor: 'pointer',
            ':hover': {
              transform: 'translateY(-5px)'
            }
          }}>
            <div style={{
              fontSize: '40px',
              marginBottom: '10px',
              textAlign: 'center'
            }}>
              {example.icon}
            </div>
            <h3 style={{
              color: '#E67E22',
              fontSize: '20px',
              marginBottom: '10px'
            }}>
              {example.field}
            </h3>
            <p style={{
              color: '#D35400',
              fontSize: '16px',
              lineHeight: '1.5'
            }}>
              {example.description}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}