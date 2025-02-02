function RealWorldExamplesCarousel() {
  const [currentIndex, setCurrentIndex] = useState(0);

  const examples = [
    {
      title: "Architecture & Engineering",
      text: "Integration helps calculate load-bearing capacities of curved structures like bridges and domes"
    },
    {
      title: "Economics", 
      text: "Finding total revenue by integrating marginal revenue curves over time"
    },
    {
      title: "Physics",
      text: "Calculating work done by varying forces by integrating force over distance"
    },
    {
      title: "Biology",
      text: "Population growth modeling using integration of growth rate functions"
    }
  ];

  const nextSlide = () => {
    setCurrentIndex((prevIndex) => 
      prevIndex === examples.length - 1 ? 0 : prevIndex + 1
    );
  };

  const prevSlide = () => {
    setCurrentIndex((prevIndex) =>
      prevIndex === 0 ? examples.length - 1 : prevIndex - 1
    );
  };

  return (
    <div style={{
      fontFamily: 'Arial',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      padding: '20px',
      backgroundColor: '#FFF5EB'
    }}>
      <h2 style={{
        color: '#FF8C00',
        fontSize: '24px',
        marginBottom: '20px'
      }}>
        Real World Applications
      </h2>

      <div style={{
        position: 'relative',
        width: '80%',
        height: '200px',
        backgroundColor: '#FFE4CC',
        borderRadius: '10px',
        padding: '20px',
        margin: '20px 0'
      }}>
        <h3 style={{
          color: '#FF7F24',
          fontSize: '20px',
          marginBottom: '10px'
        }}>
          {examples[currentIndex].title}
        </h3>
        <p style={{
          color: '#FF8C69',
          fontSize: '16px'
        }}>
          {examples[currentIndex].text}
        </p>
      </div>

      <div style={{
        display: 'flex',
        gap: '20px'
      }}>
        <button 
          onClick={prevSlide}
          style={{
            backgroundColor: '#FFA500',
            border: 'none',
            padding: '10px 20px',
            borderRadius: '5px',
            color: 'white',
            cursor: 'pointer'
          }}
        >
          Previous
        </button>
        <button 
          onClick={nextSlide}
          style={{
            backgroundColor: '#FFA500',
            border: 'none',
            padding: '10px 20px',
            borderRadius: '5px',
            color: 'white',
            cursor: 'pointer'
          }}
        >
          Next
        </button>
      </div>
    </div>
  );
}