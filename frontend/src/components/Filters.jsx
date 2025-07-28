import { useEffect } from "react";

function Dropdown({ label, id, selected, options, onChange }) {
  return (
    <div>
      <label htmlFor={`"${id}-select"`}>{label}</label>

      <select
        name={`"${id}"`}
        id={`"${id}-select"`}
        value={selected}
        onChange={(e) => onChange(e)}
      >
        <option value=""></option>
        {options.map(({ name, value }) => (
          <option key={value} value={value}>
            {name}
          </option>
        ))}
      </select>
    </div>
  );
}

function Filters({
  locations,
  metrics,
  filters,
  onFilterChange,
  onApplyFilters,
}) {
  // TODO: Implement the filters component that allows users to:
  // - Select a location from the available locations
  // - Select a climate metric from available metrics
  // - Choose a date range (start and end dates)
  // - Filter by data quality threshold
  // - Select different analysis types
  // - Apply the filters
  //
  // Requirements:
  // - Use the locations and metrics arrays passed as props
  // - Maintain filter state
  // - Call onFilterChange when filters change
  // - Call onApplyFilters when filters should be applied
  // - Use appropriate UI components (dropdowns, date pickers, etc.)
  // - Make the UI responsive and user-friendly
  // - Add any additional filtering options you think would be valuable
  const handleChange = (value) => {
    onFilterChange(value);
  };

  useEffect(() => {
    onApplyFilters();
  }, [filters]);

  return (
    <div className="bg-white p-4 rounded-lg shadow-md">
      <h2 className="text-xl font-semibold text-eco-primary mb-4">
        Filter Data
      </h2>

      <Dropdown
        label="Location: "
        id="location"
        selected={filters.locationId}
        options={locations.map(({ id, name }) => ({ name, value: id }))}
        onChange={(e) =>
          handleChange({ ...filters, locationId: e.target.value })
        }
      ></Dropdown>

      <Dropdown
        label="Metric: "
        id="metric"
        selected={filters.metric}
        options={metrics.map(({ id, display_name }) => ({
          name: display_name,
          value: id,
        }))}
        onChange={(e) => handleChange({ ...filters, metric: e.target.value })}
      ></Dropdown>

      <div>
        <label htmlFor="start-date">Start Date</label>
        <input
          id="start-date"
          type="date"
          value={filters.startDate}
          onChange={(e) =>
            handleChange({ ...filters, startDate: e.target.value })
          }
        ></input>
        <label htmlFor="end-date">End Date</label>
        <input
          id="end-date"
          type="date"
          value={filters.endDate}
          onChange={(e) =>
            handleChange({ ...filters, endDate: e.target.value })
          }
        ></input>
      </div>

      <div>
        <p>Quality Threshold:</p>

        <div>
          <input
            type="radio"
            id="quality-all"
            name="quality"
            value=""
            checked={filters.qualityThreshold === ""}
            onChange={() => handleChange({ ...filters, qualityThreshold: "" })}
          />
          <label htmlFor="quality-all">All</label>
        </div>

        <div>
          <input
            type="radio"
            id="quality-excellent"
            name="quality"
            value="excellent"
            checked={filters.qualityThreshold === "excellent"}
            onChange={() =>
              handleChange({ ...filters, qualityThreshold: "excellent" })
            }
          />
          <label htmlFor="quality-excellent">Excellent</label>
        </div>

        <div>
          <input
            type="radio"
            id="quality-good"
            name="quality"
            value="good"
            checked={filters.qualityThreshold === "good"}
            onChange={() =>
              handleChange({ ...filters, qualityThreshold: "good" })
            }
          />
          <label htmlFor="quality-good">Good</label>
        </div>

        <div>
          <input
            type="radio"
            id="quality-questionable"
            name="quality"
            value="questionable"
            checked={filters.qualityThreshold === "questionable"}
            onChange={() =>
              handleChange({ ...filters, qualityThreshold: "questionable" })
            }
          />
          <label htmlFor="quality-questionable">Questionable</label>
        </div>

        <div>
          <input
            type="radio"
            id="quality-poor"
            name="quality"
            value="poor"
            checked={filters.qualityThreshold === "poor"}
            onChange={() =>
              handleChange({ ...filters, qualityThreshold: "poor" })
            }
          />
          <label htmlFor="quality-poor">Poor</label>
        </div>
      </div>
    </div>
  );
}

export default Filters;
