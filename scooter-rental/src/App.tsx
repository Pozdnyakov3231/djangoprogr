import { useEffect, useState } from 'react';
import { Card, Button, Container, Row, Col, Badge } from 'react-bootstrap';
import axios from 'axios';

interface Scooter {
  Id: number;
  model: string;
  battery_capacity: number;
  battery_level: number;
  status: string;
  last_maintenance_date: string;
}

const API_URL = 'http://localhost:8000/nocodb-data/';

const Rental = () => {
  const [scooters, setScooters] = useState<Scooter[]>([]);

  useEffect(() => {
    axios.get(API_URL)
      .then((response) => setScooters(response.data.records))
      .catch((error) => console.error('Ошибка при загрузке данных:', error));
  }, []);

  // Функция для выбора цвета бейджа статуса
  const getStatusVariant = (status: string) => {
    switch (status) {
      case 'availible': return 'success';
      case 'rented': return 'warning';
      case 'maintenance': return 'danger';
      default: return 'secondary';
    }
  };

  return (
    <Container>
      <h1 className="my-4 text-center">Аренда самокатов</h1>
      <Row>
        {scooters.map((scooter) => (
          <Col key={scooter.Id} md={6} lg={4} className="mb-4">
            <Card>
              <Card.Body>
                <Card.Title>{scooter.model}</Card.Title>
                <Badge bg={getStatusVariant(scooter.status)} className="mb-2">
                  {scooter.status.toUpperCase()}
                </Badge>
                <Card.Text>
                  <strong>Батарея:</strong> {scooter.battery_level}% (макс. {scooter.battery_capacity}%) <br />
                  <strong>Последнее ТО:</strong> {new Date(scooter.last_maintenance_date).toLocaleDateString()}  
                </Card.Text>
                <Button 
                  variant="primary" 
                  disabled={scooter.status !== 'availible'}
                >
                  Арендовать
                </Button>
              </Card.Body>
            </Card>
          </Col>
        ))}
      </Row>
    </Container>
  );
};

export default Rental;
