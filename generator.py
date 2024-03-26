from datetime import datetime, timedelta
import random
import uuid
import time
import streamlit


class PayloadGenerator:
    @classmethod
    def generate_payloads(cls, num_payloads, start_date, end_date):
        payloads = []
        for _ in range(num_payloads):
            payload = cls.generate_payload(start_date, end_date)
            payloads.append(payload)
        return payloads

    @classmethod
    def generate_payload(cls, start_date, end_date):
        payload = {
            "iid": f"sport:{uuid.uuid4().hex}",
            "type": "sportsbook",
            "userId": str(uuid.uuid1()),
            "betSportsbook": cls.generate_bet_sportsbook(start_date, end_date),
            "updatedAt": int(datetime.now().timestamp() * 1000),
            "createdAt": int(datetime.now().timestamp() * 1000)
        }
        return payload

    @classmethod
    def generate_bet_sportsbook(cls, start_date, end_date):
        created_at = time.mktime(random_date(start_date, end_date).timetuple())
        updated_at = created_at + 211
        bet_sportsbook = {
            "id": str(uuid.uuid1()),
            "userId": str(uuid.uuid1()),
            "gameId": str(uuid.uuid1()),
            "currency": cls.generate_currency(),
            "amount": random.randint(50, 200),
            "payoutMultiplier": 1,
            "status": cls.generate_status(),
            "active": False,
            "outcomes": cls.generate_outcomes(created_at),
            "events": cls.generate_events(start_date, end_date),
            "createdAt": created_at,
            "updatedAt": updated_at
        }
        return bet_sportsbook

    @staticmethod
    def generate_outcomes(created_at):
        outcomes = []
        num_outcomes = random.randint(2, 5)
        for _ in range(num_outcomes):
            outcome = {
                "betId": str(uuid.uuid1()),
                "cancel": random.choice([True, False]),
                "createdAt": created_at,
                "fixtureId": str(uuid.uuid1()),
                "marketId": str(uuid.uuid1()),
                "odds": round(random.uniform(1.1, 2.5), 2),
                "outcomeId": str(uuid.uuid1()),
                "probabilities": round(random.uniform(0.5, 1.0), 6),
                "producer": random.randint(1, 5),
            }
            outcomes.append(outcome)
        return outcomes

    @staticmethod
    def generate_events(start_date, end_date):
        events = []
        for _ in range(random.randint(1, 5)):  # Random number of events
            event = {
                "betId": str(uuid.uuid1()),
                "dueAt": time.mktime(random_date(start_date, end_date).timetuple()),
                "id": str(uuid.uuid1()),
                "message": random.choice(["Match is active", "Match is not active", "Match is postponed"]),
                "processed": random.choice([True, False]),
                "type": random.choice(["accepted", "rejected"])
            }
            events.append(event)
        return events

    @staticmethod
    def generate_currency():
        currencies = ["usdt", "btc", "eth", "eur", "gbp", "jpy"]
        return random.choice(currencies)

    @staticmethod
    def generate_status():
        statuses = ["accepted", "rejected", "pending"]
        return random.choice(statuses)


def random_date(start, end):
    result = start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))
    return result
