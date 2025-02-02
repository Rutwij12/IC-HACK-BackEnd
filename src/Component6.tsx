function MusicMathDiagram() {
  return (
    <div style={{
      fontFamily: 'Arial',
      padding: '20px',
      maxWidth: '800px',
      margin: '0 auto'
    }}>
      <h2 style={{
        color: '#FF7F00',
        fontSize: '28px',
        marginBottom: '20px'
      }}>
        Pythagorean Musical Ratios
      </h2>
      
      <div style={{
        display: 'flex',
        justifyContent: 'space-between',
        marginBottom: '40px'
      }}>
        <div style={{
          border: '2px solid #FFB366',
          padding: '15px',
          borderRadius: '8px',
          width: '45%'
        }}>
          <h3 style={{color: '#FF8C1A', marginBottom: '10px'}}>
            String Length Ratios
          </h3>
          <svg width="200" height="120">
            <line x1="20" y1="20" x2="180" y2="20" stroke="#FF9933" strokeWidth="2"/>
            <text x="85" y="15" style={{fill: '#FF9933'}}>1:1 (Unison)</text>
            
            <line x1="20" y1="60" x2="100" y2="60" stroke="#FF9933" strokeWidth="2"/>
            <text x="85" y="55" style={{fill: '#FF9933'}}>2:1 (Octave)</text>
            
            <line x1="20" y1="100" x2="140" y2="100" stroke="#FF9933" strokeWidth="2"/>
            <text x="85" y="95" style={{fill: '#FF9933'}}>3:2 (Fifth)</text>
          </svg>
        </div>

        <div style={{
          border: '2px solid #FFB366',
          padding: '15px', 
          borderRadius: '8px',
          width: '45%'
        }}>
          <h3 style={{color: '#FF8C1A', marginBottom: '10px'}}>
            Sound Wave Patterns
          </h3>
          <svg width="200" height="120">
            <path d="M 10 60 Q 52.5 20, 95 60 T 180 60" 
                  fill="none" 
                  stroke="#FF9933" 
                  strokeWidth="2"/>
            <path d="M 10 60 Q 35 100, 60 60 T 110 60" 
                  fill="none" 
                  stroke="#FF9933" 
                  strokeWidth="2"/>
          </svg>
        </div>
      </div>

      <p style={{
        color: '#FF944D',
        fontSize: '16px',
        lineHeight: '1.5',
        textAlign: 'center'
      }}>
        Pythagoras discovered that pleasant musical intervals correspond to simple whole-number ratios.
        When string lengths have ratios of 2:1, they produce an octave; 3:2 creates a perfect fifth.
      </p>
    </div>
  );
}