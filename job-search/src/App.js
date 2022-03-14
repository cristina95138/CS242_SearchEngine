import logo from './logo.svg';
import './App.css';
import TextField from "@mui/material/TextField";

function App() {
    return (
        <div className="App">
            <TextField
                id="outlined-basic"
                variant="outlined"
                fullWidth
                label="Search"
            />
        </div>
    );
}

export default App;