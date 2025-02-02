function EigenvectorDefinitionText() {
  return (
    <div style={{
      fontFamily: 'Arial',
      maxWidth: '800px',
      margin: '20px',
      color: '#CC7000'
    }}>
      <h2 style={{
        fontSize: '28px',
        color: '#FF8C00',
        marginBottom: '20px'
      }}>
        Understanding Eigenvectors - The Simple Way
      </h2>

      <p style={{
        fontSize: '18px',
        lineHeight: '1.6',
        marginBottom: '15px'
      }}>
        Think of an eigenvector like a special arrow that keeps pointing in the same direction even when you perform a transformation on it. Imagine you have a blanket, and you're stretching or squishing it - an eigenvector would be like a line drawn on that blanket that maintains its direction, even though it might get longer or shorter.
      </p>

      <p style={{
        fontSize: '18px',
        lineHeight: '1.6',
        marginBottom: '15px'
      }}>
        Here's another way to think about it: Picture a merry-go-round. Most points on the merry-go-round move in circles when it spins, but the center point stays in place - it just rotates. This center point is like an eigenvector of the spinning transformation.
      </p>

      <p style={{
        fontSize: '18px',
        lineHeight: '1.6'
      }}>
        In everyday terms, eigenvectors are like the "natural" directions of a transformation - they're the special directions where the transformation's effect is simplest, just stretching or shrinking along that direction, nothing more complicated.
      </p>
    </div>
  );
}