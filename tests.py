import unittest

from unittest.mock import Mock, patch

from main import app


class TestTbaPy3(unittest.TestCase):
    def setUp(self) -> None:
        self.client = app.test_client(self)

    def test_root(self) -> None:
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)

    @patch("models.team.Team.get_by_id")
    @patch("google.cloud.ndb.Client")
    def test_team_info(self, mock_ndb_client: Mock, mock_team_get: Mock) -> None:
        resp = self.client.get("/team/frc254")
        self.assertEqual(resp.status_code, 200)


if __name__ == "__main__":
    unittest.main()
