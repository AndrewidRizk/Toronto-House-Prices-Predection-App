import React, { useState, useEffect, useRef  } from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import axios from 'axios';
import { Line } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from 'chart.js';


// Add Leaflet's default marker icon manually
import L from 'leaflet';
import markerIcon2x from 'leaflet/dist/images/marker-icon-2x.png';
import markerIcon from 'leaflet/dist/images/marker-icon.png';
import markerShadow from 'leaflet/dist/images/marker-shadow.png';

// Register the required Chart.js components
ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);


let DefaultIcon = L.icon({
  iconUrl: markerIcon,
  iconRetinaUrl: markerIcon2x,
  shadowUrl: markerShadow,
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41],
});

L.Marker.prototype.options.icon = DefaultIcon;

const containerStyle = {
    width: '100%',
    height: '600px',
};

const center = [43.7, -79.42];

// Sample community locations with lat/lng
// Sample community locations with lat/lng
const communityLocations = [
    { name: "Agincourt North", lat: 43.8080383, lng: -79.2664391 },
    { name: "Alderwood", lat: 43.6017173, lng: -79.5452325 },
    { name: "Annex", lat: 43.6703045, lng: -79.4052888 },
    { name: "Banbury-Don Mills", lat: 43.7526832, lng: -79.3652703 },
    { name: "Bathurst Manor", lat: 43.76389295, lng: -79.45636693710946 },
    { name: "Bay Street Corridor", lat: 43.6701851, lng: -79.3902694 },
    { name: "Bayview Village", lat: 43.7666288, lng: -79.3880087 },
    { name: "Bayview Woods-Steeles", lat: 43.79643345, lng: -79.38203447034945 },
    { name: "Bendale", lat: 43.7535196, lng: -79.2553355 },
    { name: "Black Creek", lat: 43.6954005, lng: -79.485495 },
    { name: "Blake-Jones", lat: 43.6751574, lng: -79.3405447 },
    { name: "Briar Hill-Belgravia", lat: 43.7031939, lng: -79.4489697 },
    { name: "Broadview North", lat: 43.6839216, lng: -79.3569421 },
    { name: "Caledonia-Fairbank", lat: 43.6931938, lng: -79.4618638 },
    { name: "Casa Loma", lat: 43.6781015, lng: -79.4094158929368 },
    { name: "Centennial Scarborough", lat: 43.7874914, lng: -79.1507681 },
    { name: "Clanton Park", lat: 43.7419002, lng: -79.441675 },
    { name: "Cliffcrest", lat: 43.7218363, lng: -79.2362138 },
    { name: "Corso Italia-Davenport", lat: 43.677954, lng: -79.4430828 },
    { name: "Crescent Town", lat: 43.695403, lng: -79.293099 },
    { name: "Danforth", lat: 43.6864333, lng: -79.3003555 },
    { name: "Danforth Village-East York", lat: 43.6833573, lng: -79.3235744 },
    { name: "Don Valley Village", lat: 43.7926732, lng: -79.3547219 },
    { name: "Dorset Park", lat: 43.7528467, lng: -79.282067 },
    { name: "Dovercourt-Wallace Emerson-Junction", lat: 43.668005, lng: -79.4413386 },
    { name: "Dufferin Grove", lat: 43.6536319, lng: -79.4264389 },
    { name: "East End-Danforth", lat: 43.6684402, lng: -79.33067 },
    { name: "East York", lat: 43.699971, lng: -79.33251996261595 },
    { name: "Edenbridge-Humber Valley", lat: 43.670672, lng: -79.5188545 },
    { name: "Eglinton East", lat: 43.73049015, lng: -79.28299031923446 },
    { name: "Englemount-Lawrence", lat: 43.7123465, lng: -79.434661 },
    { name: "Etobicoke West Mall", lat: 43.6346909, lng: -79.5620422 },
    { name: "Flemingdon Park", lat: 43.7184315, lng: -79.333204 },
    { name: "Forest Hill North", lat: 43.7040939, lng: -79.4328647 },
    { name: "Guildwood", lat: 43.7552251, lng: -79.1982293 },
    { name: "Henry Farm", lat: 43.7695089, lng: -79.354296 },
    { name: "High Park North", lat: 43.6573833, lng: -79.470961 },
    { name: "High Park-Swansea", lat: 43.6495416, lng: -79.4842102 },
    { name: "Highland Creek", lat: 43.7901172, lng: -79.1733344 },
    { name: "Hillcrest Village", lat: 43.7996637, lng: -79.3650189 },
    { name: "Humber Heights", lat: 43.6981503, lng: -79.5232733 },
    { name: "Humber Summit", lat: 43.7600778, lng: -79.5717598 },
    { name: "Humbermede", lat: 43.7477297, lng: -79.5479358 },
    { name: "Humewood-Cedarvale", lat: 43.6883215, lng: -79.4280805 },
    { name: "Ionview", lat: 43.7359904, lng: -79.2765146 },
    { name: "Islington-City Centre West", lat: 43.6796914, lng: -79.5392004 },
    { name: "Keelesdale-Eglinton West", lat: 43.6904322, lng: -79.474876 },
    { name: "Kennedy Park", lat: 43.7160528, lng: -79.2606869 },
    { name: "Kingsway South", lat: 43.6415777, lng: -79.47989252624168 },
    { name: "L'Amoreaux", lat: 43.799003, lng: -79.3059669 },
    { name: "Lambton Baby Point", lat: 43.6558741, lng: -79.4964941 },
    { name: "Lawrence Park North", lat: 43.7416009, lng: -79.3097502 },
    { name: "Leaside", lat: 43.7047983, lng: -79.3680904 },
    { name: "Little Portugal", lat: 43.64741325, lng: -79.4311169602729 },
    { name: "Long Branch", lat: 43.59200455, lng: -79.54536450659592 },
    { name: "Malvern", lat: 43.8091955, lng: -79.2217008 },
    { name: "Maple Leaf", lat: 43.7122767, lng: -79.4901977 },
    { name: "Markland Wood", lat: 43.6342017, lng: -79.5693915 },
    { name: "Milliken", lat: 43.8190311, lng: -79.28593195098604 },
    { name: "Mimico", lat: 43.6166773, lng: -79.4968048 },
    { name: "Morningside", lat: 43.7826012, lng: -79.2049579 },
    { name: "Moss Park", lat: 43.6546438, lng: -79.3697278 },
    { name: "Mount Dennis", lat: 43.6869597, lng: -79.4895513 },
    { name: "Mount Pleasant East", lat: 43.7043827, lng: -79.3879674 },
    { name: "Mount Pleasant West", lat: 43.7085752, lng: -79.3904738 },
    { name: "New Toronto", lat: 43.6007625, lng: -79.505264 },
    { name: "Niagara", lat: 43.6440753, lng: -79.4086982 },
    { name: "North Riverdale", lat: 43.6743543, lng: -79.3539116 },
    { name: "O'Connor-Parkview", lat: 43.6999213, lng: -79.3194177 },
    { name: "Oakridge", lat: 43.6971738, lng: -79.2748232 },
    { name: "Oakwood-Vaughan", lat: 43.6920025, lng: -79.4398661 },
    { name: "Palmerston-Little Italy", lat: 43.653854, lng: -79.4092999 },
    { name: "Playter Estates-Danforth", lat: 43.6789325, lng: -79.3554539 },
    { name: "Pleasant View", lat: 43.787048, lng: -79.3337137 },
    { name: "Regent Park", lat: 43.6607056, lng: -79.3604569 },
    { name: "Rexdale-Kipling", lat: 43.7115046, lng: -79.5663897 },
    { name: "Rockcliffe-Smythe", lat: 43.677044, lng: -79.4761512 },
    { name: "Roncesvalles", lat: 43.6474601, lng: -79.4494931 },
    { name: "Rosedale-Moore Park", lat: 43.6785796, lng: -79.38043658 },
    { name: "Rouge E10", lat: 43.8049304, lng: -79.1658374 },
    { name: "Rouge E11", lat: 43.8049304, lng: -79.1658374 },
    { name: "Runnymede-Bloor West Village", lat: 43.6509753, lng: -79.4762323 },
    { name: "Rustic", lat: 43.71336615, lng: -79.50450373904313 },
    { name: "Scarborough Village", lat: 43.7437422, lng: -79.2116324 },
    { name: "South Parkdale", lat: 43.636321, lng: -79.4753929 },
    { name: "South Riverdale", lat: 43.6624452, lng: -79.3513464 },
    { name: "Steeles", lat: 43.8161778, lng: -79.3145378 },
    { name: "Stonegate-Queensway", lat: 43.6239367, lng: -79.5124094 },
    { name: "Tam O'Shanter-Sullivan", lat: 43.7792808, lng: -79.3036989 },
    { name: "The Beaches", lat: 43.6710244, lng: -79.296712 },
    { name: "Thistletown-Beaumonde Heights", lat: 43.738174, lng: -79.5652117 },
    { name: "Thorncliffe Park", lat: 43.704553, lng: -79.3454074 },
    { name: "Trinity-Bellwoods", lat: 43.647644, lng: -79.41391219789621 },
    { name: "Victoria Village", lat: 43.732658, lng: -79.3111892 },
    { name: "West Hill", lat: 43.7689144, lng: -79.1872905 },
    { name: "West Humber-Clairville", lat: 43.71321895, lng: -79.59225148604071 },
    { name: "Weston", lat: 43.7001711, lng: -79.5162093 },
    { name: "Willowdale East", lat: 43.764756, lng: -79.396899 },
    { name: "Willowdale West", lat: 43.76084865, lng: -79.4121268006679 },
    { name: "Woburn", lat: 43.7598243, lng: -79.2252908 },
    { name: "Wychwood", lat: 43.68218115, lng: -79.42305519894066 },
    { name: "Yonge-Eglinton", lat: 43.7067479, lng: -79.3983271 },
    { name: "Yonge-St. Clair", lat: 43.687336, lng: -79.393238 },
    { name: "York University Heights", lat: 43.7648127, lng: -79.5012796 },
    { name: "Yorkdale-Glen Park", lat: 43.7064433, lng: -79.4526856 }
];

const Map = () => {
    const [selectedCommunity, setSelectedCommunity] = useState(null);
    const [housingData, setHousingData] = useState(null);
    const [chartData, setChartData] = useState(null);
    const infoPanelRef = useRef(null); // Reference for the info panel

    // Scroll to the info panel when a marker is clicked
    const handleMarkerClick = (community) => {
        setSelectedCommunity(community);
        if (infoPanelRef.current) {
            infoPanelRef.current.scrollIntoView({ behavior: 'smooth' });
        }
    };


    const fetchCommunityData = async (communityName) => {
        try {
            
            const response = await axios.post('https://5ebf-76-68-94-132.ngrok-free.app/community-data', {
                community: communityName,
            });
            setHousingData(response.data);
        } catch (error) {
            console.error("Error fetching data:", error);
            setHousingData(null);
        }
    };

    useEffect(() => {
        if (housingData && selectedCommunity) {
            const labels = ['2022', '2023', '2024/2025']; // X-axis labels for the chart
            const datasets = Object.keys(housingData).map((buildingType) => ({
                label: buildingType,
                data: [
                    parseFloat(housingData[buildingType]['2022'].replace('CAD$', '').replace(',', '')),
                    parseFloat(housingData[buildingType]['2023'].replace('CAD$', '').replace(',', '')),
                    parseFloat(housingData[buildingType]['Predicted 2024/2025'].replace('CAD$', '').replace(',', ''))
                ],
                borderColor: getRandomColor(), // Each building type will have a different line color
                fill: false,
            }));

            setChartData({
                labels: labels,
                datasets: datasets
            });
        }
    }, [housingData, selectedCommunity]);

    // Function to generate a random color for the chart lines
    const getRandomColor = () => {
        const letters = '0123456789ABCDEF';
        let color = '#';
        for (let i = 0; i < 6; i++) {
            color += letters[Math.floor(Math.random() * 16)];
        }
        return color;
    };

    return (
        <div className="layout">
            <header className="header">
                <h1>Toronto Housing Insights</h1> {/* Updated the app name */}
            </header>

            <div className="content">
                <div className="map-container">
                    <label>Choose one of the following communities:</label>
                    <MapContainer style={containerStyle} center={center} zoom={12}>
                        <TileLayer
                            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                            attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                        />
                        {communityLocations.map((community, index) => (
                            <Marker
                                key={index}
                                position={[community.lat, community.lng]}
                                eventHandlers={{
                                    click: () => {
                                        setSelectedCommunity(community);
                                        fetchCommunityData(community.name);
                                        handleMarkerClick(community);
                                    },
                                }}
                            >
                                <Popup>
                                    <strong>{community.name}</strong>
                                </Popup>
                            </Marker>
                        ))}
                    </MapContainer>
                </div>

                <div className="info-panel" ref={infoPanelRef}>
                    {selectedCommunity ? (
                        <div>
                            <h3>{selectedCommunity.name}</h3>

                            <h4>Housing Data:</h4>
                            {housingData ? (
                                <>
                                    {chartData && (
                                        <div style={{ marginBottom: '20px' }}>
                                            <Line 
                                                data={chartData} 
                                                options={{
                                                    responsive: true,
                                                    plugins: {
                                                        legend: {
                                                            position: 'top',
                                                        },
                                                        title: {
                                                            display: true,
                                                            text: `Housing Price Trends for ${selectedCommunity.name}`,
                                                        },
                                                    },
                                                }} 
                                            />
                                        </div>
                                    )}

                                    {Object.keys(housingData).map((buildingType) => (
                                        <div key={buildingType}>
                                            <strong>{buildingType}</strong>
                                            <p>2022 Price: {housingData[buildingType]['2022']}</p>
                                            <p>2023 Price: {housingData[buildingType]['2023']}</p>
                                            <p>Predicted 2024/2025 Price: {housingData[buildingType]['Predicted 2024/2025']}</p>
                                            <div className="separator" />
                                        </div>
                                    ))}
                                </>
                            ) : (
                                <p>Loading data...</p>
                            )}
                        </div>
                    ) : (
                        <p>Select a community on the map to see housing data.</p>
                    )}
                </div>
            </div>

            <footer className="footer">
                Made by <a href="https://www.androrizk.com" target="_blank" rel="noopener noreferrer">Andro Rizk</a>
            </footer>
        </div>
    );
};

export default Map;