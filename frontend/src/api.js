/**
 * API service module for making requests to the backend
 */

// TODO Implement a way to switch between dev/prod configs at build time
const API_BASE_URL = "http://127.0.0.1:8000/api/v1";

/**
 * Fetch climate data with optional filters
 * @param {Object} filters - Filter parameters
 * @returns {Promise} - API response
 */
export const getClimateData = async (filters = {}) => {
  try {
    let endpoint = `${API_BASE_URL}/climate`;

    // TODO: Implement filters
    const queryParams = new URLSearchParams({
      ...(filters.locationId && { location_id: filters.locationId }),
      ...(filters.startDate && { start_date: filters.startDate }),
      ...(filters.endDate && { end_date: filters.endDate }),
      ...(filters.metric && { metric: filters.metric }),
      ...(filters.qualityThreshold && {
        quality_threshold: filters.qualityThreshold,
      }),
    });

    console.log(`fetching ${endpoint}`);
    const response = await fetch(`${endpoint}?${queryParams}`);
    const data = await response.json();

    return data;
  } catch (error) {
    console.error('API Error:', error);
    throw error;
  }
};

/**
 * Fetch all available locations
 * @returns {Promise} - API response
 */
export const getLocations = async () => {
  try {
    let endpoint = `${API_BASE_URL}/locations`;

    console.log(`fetching ${endpoint}`);
    const response = await fetch(`${endpoint}`);
    const data = await response.json();

    return data;
  } catch (error) {
    console.error('API Error:', error);
    throw error;
  }
};

/**
 * Fetch all available metrics
 * @returns {Promise} - API response
 */
export const getMetrics = async () => {
  try {
    let endpoint = `${API_BASE_URL}/metrics`;

    console.log(`fetching ${endpoint}`);
    const response = await fetch(`${endpoint}`);
    const data = await response.json();

    return data;
  } catch (error) {
    console.error('API Error:', error);
    throw error;
  }
};

/**
 * Fetch climate summary statistics with optional filters
 * @param {Object} filters - Filter parameters
 * @returns {Promise} - API response
 */
export const getClimateSummary = async (filters = {}) => {
  try {
    // TODO: Implement API call with filters
  } catch (error) {
    console.error('API Error:', error);
    throw error;
  }
};