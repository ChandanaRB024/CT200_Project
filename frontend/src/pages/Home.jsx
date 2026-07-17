import { useState, useRef } from "react";
import api from "../services/api";
import "../App.css";

function Home() {

  const [message, setMessage] = useState("");
  const [nodes, setNodes] = useState([]);
  const [testCases, setTestCases] = useState("");
  const [loading, setLoading] = useState(false);

  const resultRef = useRef(null);

  const importV1 = async () => {
    try {
      const res = await api.post("/import/v1");
      setMessage(res.data.message);
    } catch {
      setMessage("Import Version 1 Failed");
    }
  };

  const importV2 = async () => {
    try {
      const res = await api.post("/import/v2");
      setMessage(res.data.message);
    } catch {
      setMessage("Import Version 2 Failed");
    }
  };

  const compareVersions = async () => {
    try {
      await api.get("/compare");
      setMessage("Comparison Completed Successfully");
    } catch {
      setMessage("Comparison Failed");
    }
  };

  const loadNodes = async () => {
    try {
      const res = await api.get("/nodes/1");
      setNodes(res.data);
      setTestCases("");
      setMessage("Document Sections Loaded Successfully");
    } catch {
      setMessage("Unable to Load Nodes");
    }
  };

  const generateTestCases = async (nodeId) => {

    setLoading(true);

    try {

      const res = await api.get(`/generate/${nodeId}`);

      let cleaned = res.data.test_cases
        .replace(/###/g, "")
        .replace(/\*\*/g, "")
        .replace(/```/g, "")
        .replace(/---/g, "")
        .trim();

      setTestCases(cleaned);

      setTimeout(() => {
        resultRef.current?.scrollIntoView({
          behavior: "smooth"
        });
      }, 300);

    } catch {

      setTestCases("Failed to Generate Test Cases");

    }

    setLoading(false);

  };

  return (

    <div className="container">

      <h1>🤖 CT200 AI Document Management System</h1>

      <div className="button-group">

        <button onClick={importV1}>
          📥 Import Version 1
        </button>

        <button onClick={importV2}>
          📥 Import Version 2
        </button>

        <button onClick={compareVersions}>
          🔄 Compare Versions
        </button>

        <button onClick={loadNodes}>
          📑 Load Sections
        </button>

      </div>

      {message &&

        <div className="message">

          {message}

        </div>

      }

      {nodes.length > 0 && (

        <>

          <h2>📚 Document Sections</h2>

          {nodes
            .filter(node => node.level > 1)
            .map(node => (

              <div className="card" key={node.id}>

                <h3>{node.heading}</h3>

                <button
                  onClick={() => generateTestCases(node.id)}
                >
                  🤖 Generate Test Cases
                </button>

              </div>

            ))}

        </>

      )}

      {loading &&

        <h2>

          🤖 AI is generating test cases...

        </h2>

      }

      {testCases && (

        <div
          className="result"
          ref={resultRef}
        >

          <h2>

            ✨ AI Generated Functional Test Cases

          </h2>

          <pre>

            {testCases}

          </pre>

        </div>

      )}

    </div>

  );

}

export default Home;