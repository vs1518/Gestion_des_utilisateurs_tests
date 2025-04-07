import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '2s', target: 2 },
    { duration: '2s', target: 2 },
    { duration: '2s', target: 0 },
  ],
};

export default function () {
    const url = 'http://localhost/Gestion_des_utilisateurs_tests/api.php';

  const name = `User${Math.floor(Math.random() * 10000)}`;
  const email = `user${Math.floor(Math.random() * 10000)}@test.com`;
  const payload = `name=${encodeURIComponent(name)}&email=${encodeURIComponent(email)}`;

  const params = {
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
  };

  const res = http.post(url, payload, params);

  check(res, {
    'statut 200': (r) => r.status === 200,
    'réponse correcte': (r) => r.body.includes(name) || r.body.includes('ajouté'),
  });

  sleep(1);
}
