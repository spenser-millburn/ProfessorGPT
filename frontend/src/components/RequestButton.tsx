import { Button } from '@mui/material';
import React from 'react';

interface RequestButtonProps {
  url: string,
  requestType: string,
  responseHandler: (data:any) => void
}

/**
 * Represents a button component used for making API requests.
 *
 * @component
 * @param {string} url - The URL to make the API request to.
 * @param {string} requestType - The type of HTTP request to make.
 * @param {(data: any) => void} responseHandler - The callback function to handle the response data.
 * @returns {React.FC} - The RequestButton component.
 */
const RequestButton: React.FC<RequestButtonProps> = ({ url, requestType, responseHandler }) => {
  /**
   * Handles the click event of the button and makes the API request.
   */
  const handleClick = () => {
    fetch(url, { method: requestType })
      .then(response => response.json())
      .then(data => {
        console.log(data);
        responseHandler(data);
      })
      .catch(error => {
        // Handle the error
        console.error('Error:', error);
      });
  };

  return (
    <Button variant="outlined" color="primary" onClick={handleClick}>
      Get Routes
    </Button>
  );
};

export default RequestButton;
