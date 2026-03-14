import pytest
from pages.vehicle_dashboard_page import VehicleDashboardPage

@pytest.mark.parametrize("username,password,expected_parts", [
    ("standard_user", "secret_sauce", 6),
    ("problem_user", "secret_sauce", 6),
])
def test_vehicle_dashboard_login_and_wireless(driver, username, password, expected_parts):
    page = VehicleDashboardPage(driver)
    page.open("https://www.saucedemo.com")

    page.login(username, password)
    status = page.get_wireless_status()
    parts = page.get_vehicle_parts_count()

    assert "Swag Labs" in driver.title, "Vehicle dashboard failed to load"
    assert "Products" in status, "Wireless/network dashboard header not visible"
    assert parts == expected_parts, f"Expected {expected_parts} vehicle components, got {parts}"
