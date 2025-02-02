function TimelineBanner() {
  const [selectedEvent, setSelectedEvent] = useState(null);

  const events = [
    {
      year: "570 BCE",
      title: "Birth",
      details: "Born on the island of Samos, Greece"
    },
    {
      year: "535 BCE", 
      title: "Migration to Italy",
      details: "Established his school in Croton"
    },
    {
      year: "532 BCE",
      title: "Pythagoras' Theorem",
      details: "Formalized the relationship between sides of right triangles"
    },
    {
      year: "520 BCE",
      title: "Music Theory",
      details: "Discovered mathematical ratios in musical harmonies"
    },
    {
      year: "495 BCE",
      title: "Death",
      details: "Died in Metapontum, Italy"
    }
  ];

  const timelineStyles = {
    container: {
      padding: "20px",
      fontFamily: "Arial",
      position: "relative"
    },
    line: {
      height: "4px",
      backgroundColor: "#FFA500",
      width: "100%",
      margin: "50px 0"
    },
    events: {
      display: "flex",
      justifyContent: "space-between",
      position: "relative"
    },
    event: {
      cursor: "pointer",
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      width: "120px"
    },
    dot: {
      width: "20px",
      height: "20px",
      borderRadius: "50%",
      backgroundColor: "#FF8C00",
      margin: "10px 0"
    },
    year: {
      color: "#FF6600",
      fontWeight: "bold"
    },
    selectedEvent: {
      position: "absolute",
      top: "100px",
      left: "50%",
      transform: "translateX(-50%)",
      backgroundColor: "#FFF3E0",
      padding: "15px",
      borderRadius: "8px",
      boxShadow: "0 2px 4px rgba(0,0,0,0.1)",
      color: "#FF8C00",
      textAlign: "center"
    }
  };

  return (
    <div style={timelineStyles.container}>
      <h2 style={{color: "#FF4500", fontSize: "24px", textAlign: "center"}}>
        Pythagoras Timeline
      </h2>
      <div style={timelineStyles.line} />
      <div style={timelineStyles.events}>
        {events.map((event, index) => (
          <div 
            key={index}
            style={timelineStyles.event}
            onClick={() => setSelectedEvent(event)}
          >
            <div style={timelineStyles.dot} />
            <span style={timelineStyles.year}>{event.year}</span>
          </div>
        ))}
      </div>
      {selectedEvent && (
        <div style={timelineStyles.selectedEvent}>
          <h3 style={{color: "#FF4500", margin: "0 0 10px 0"}}>
            {selectedEvent.title}
          </h3>
          <p style={{color: "#FF8C00", margin: 0}}>
            {selectedEvent.details}
          </p>
        </div>
      )}
    </div>
  );
}