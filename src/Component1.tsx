function SetDefinitionCard() {
  return (
    <div style={{
      fontFamily: 'Arial',
      padding: '20px',
      maxWidth: '600px',
      borderRadius: '8px',
      backgroundColor: '#fff6eb'  
    }}>
      <h2 style={{
        fontSize: '24px',
        color: '#e65c00',
        marginBottom: '15px'
      }}>
        What is a Mathematical Set?
      </h2>
      
      <p style={{
        fontSize: '16px',
        color: '#cc5200',
        lineHeight: '1.6',
        marginBottom: '15px'
      }}>
        A set is a collection of distinct objects, considered as a single unit. The objects in a set are called elements or members of the set. Sets are usually denoted by capital letters.
      </p>

      <div style={{
        fontSize: '16px',
        color: '#e67300',
        marginBottom: '15px'
      }}>
        <h3 style={{
          fontSize: '18px',
          color: '#cc5200',
          marginBottom: '10px'
        }}>
          Simple Examples:
        </h3>
        <ul style={{lineHeight: '1.6'}}>
          <li>A = {'{'}1, 2, 3, 4, 5{'}'} is a set of first five natural numbers</li>
          <li>B = {'{'}red, blue, green{'}'} is a set of colors</li>
          <li>C = {'{'}dog, cat, rabbit{'}'} is a set of animals</li>
        </ul>
      </div>

      <p style={{
        fontSize: '16px',
        color: '#cc5200',
        fontStyle: 'italic'
      }}>
        Key characteristic: Each element in a set must be unique, and the order of elements doesn't matter.
      </p>
    </div>
  );
}