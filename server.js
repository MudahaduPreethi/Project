const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const dotenv = require('dotenv');
const mongoose = require('mongoose');

dotenv.config();

const app = express();

// Middlewares
app.use(bodyParser.json());
app.use(cors());

// Connect to MongoDB
mongoose.connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('MongoDB connected'))
  .catch(err => console.log(err));

// Home Route
app.get('/', (req, res) => {
    res.send('Welcome to the Agriculture Backend');
});

// Define the User schema
const userSchema = new mongoose.Schema({
    username: String,
    password: String,
});

// Create the User model
const User = mongoose.model('User', userSchema);

// Route for Login (POST)
app.post('/login', async (req, res) => {
    const { username, password } = req.body;
    try {
        const user = await User.findOne({ username });
        if (user && user.password === password) {
            res.status(200).send('Login Successful');
        } else {
            res.status(400).send('Invalid Credentials');
        }
    } catch (error) {
        res.status(500).send('Error occurred');
    }
});

// Start Server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
