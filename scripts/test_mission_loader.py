from omokai_executor.mission_loader import MissionLoader


def main():
    mission = MissionLoader.load("missions/warehouse_loop.json")

    print("Mission Loaded Successfully!")
    print(mission)


if __name__ == "__main__":
    main()