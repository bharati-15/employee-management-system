import React from "react";
import { Container, Box, Typography, TextField, Button, Paper} from "@mui/material";
import {Link, useLocation} from 'react-router-dom';

const Login = () => {
  return (
    <Container maxWidth="sm">
      <Box
        sx={{
          height: "100vh",
          display: "flex",
          alignItems: "flex-start",
          justifyContent: "center",
          mt: 10
        }}
      >
        <Paper elevation={3} sx={{ padding: 4, width: "100%" }}>
          <Typography variant="h5" align="center" gutterBottom>
            Login to your account
          </Typography>

          <Box component="form" sx={{ mt: 2 }}>
            <TextField
              label="Email"
              type="email"
              variant="outlined"
              fullWidth
              margin="normal"
            />

            <TextField
              label="Password"
              type="password"
              variant="outlined"
              fullWidth
              margin="normal"
            />

            <Button
              variant="contained"
              fullWidth
              sx={{ mt: 2 }}
            >
              Login
            </Button>

            {/* Forgot Password */}
            <Typography align="right" sx={{ mt: 1 }}>
              <Link href="#" underline="hover">
                Forgot password?
              </Link>
            </Typography>

            {/* Register */}
            <Typography align="center" sx={{ mt: 2 }}>
              Don't have an account?{" "}
              <Link href="/register" underline="hover">
                Register
              </Link>
            </Typography>
          </Box>
        </Paper>
      </Box>
    </Container>
  );
};

export default Login;