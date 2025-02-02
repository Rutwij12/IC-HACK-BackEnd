function IntegrationTypesGrid() {
  const integrationTypes = [
    {
      title: "API Integration",
      description: "Direct communication between systems using REST or GraphQL APIs"
    },
    {
      title: "Webhook Integration", 
      description: "Event-driven integration using HTTP callbacks"
    },
    {
      title: "File-based Integration",
      description: "Exchange of data through file transfers (CSV, XML, JSON)"
    },
    {
      title: "Database Integration",
      description: "Direct database connections and synchronization"
    },
    {
      title: "Message Queue",
      description: "Asynchronous communication using message brokers"
    },
    {
      title: "SDK Integration",
      description: "Using software development kits for native integration"
    }
  ];

  return (
    <div style={{
      fontFamily: 'Arial',
      padding: '20px'
    }}>
      <h1 style={{
        color: '#FF8C00',
        fontSize: '2em',
        marginBottom: '30px'
      }}>
        Integration Types
      </h1>
      
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))',
        gap: '20px'
      }}>
        {integrationTypes.map((type, index) => (
          <div key={index} style={{
            padding: '20px',
            border: '2px solid #FFA500',
            borderRadius: '8px',
            backgroundColor: '#FFF8DC'
          }}>
            <h3 style={{
              color: '#FF4500',
              marginBottom: '10px',
              fontSize: '1.2em'
            }}>
              {type.title}
            </h3>
            <p style={{
              color: '#FF8C00',
              fontSize: '0.9em',
              lineHeight: '1.4'
            }}>
              {type.description}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}