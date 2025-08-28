class Smartphone:
    """Base class for all smartphones"""
    def __init__(self, brand, model, os, storage_gb, battery_capacity):
        self.brand = brand
        self.model = model
        self.os = os
        self._storage_used = 0  # Encapsulated attribute
        self.storage_total = storage_gb
        self.battery_level = battery_capacity
        self.screen_on = False
    
    def install_app(self, app_name, size_gb):
        """Polymorphic method to be overridden by subclasses"""
        if self._storage_used + size_gb > self.storage_total:
            raise ValueError("Not enough storage space")
        self._storage_used += size_gb
        return f"Installed {app_name} ({size_gb}GB)"
    
    def toggle_screen(self):
        self.screen_on = not self.screen_on
        return f"Screen {'ON' if self.screen_on else 'OFF'}"
    
    def check_storage(self):
        return f"Storage: {self._storage_used}/{self.storage_total}GB used"
    
    def charge(self, percentage):
        self.battery_level = min(100, self.battery_level + percentage)
        return f"Charged to {self.battery_level}%"
    
    def perform_task(self):
        """Abstract method for polymorphism"""
        raise NotImplementedError("Subclasses must implement perform_task()")
    
    def __str__(self):
        return f"{self.brand} {self.model} ({self.os})"

class GamingPhone(Smartphone):
    """Specialized smartphone for gaming"""
    def __init__(self, brand, model, os, storage_gb, battery_capacity, gpu, cooling_system):
        super().__init__(brand, model, os, storage_gb, battery_capacity)
        self.gpu = gpu
        self.cooling_system = cooling_system
        self.game_mode = False
    
    def enable_game_mode(self):
        self.game_mode = True
        return "Game mode activated "
    
    def perform_task(self):
        self.battery_level -= 15
        return "Running AAA game "
    
    def install_app(self, app_name, size_gb):
        if "game" in app_name.lower():
            size_gb *= 0.8  # 20% size reduction for games
        return super().install_app(app_name, size_gb)

class CameraPhone(Smartphone):
    """Specialized smartphone for photography"""
    def __init__(self, brand, model, os, storage_gb, battery_capacity, 
                 main_camera_mp, zoom_level):
        super().__init__(brand, model, os, storage_gb, battery_capacity)
        self.main_camera_mp = main_camera_mp
        self.zoom_level = zoom_level
        self.night_mode = False
    
    def enable_night_mode(self):
        self.night_mode = True
        return "Night mode activate"
    
    def perform_task(self):
        self.battery_level -= 8
        return "Capturing 100MP ultra-detailed photo 📸"
    
    def install_app(self, app_name, size_gb):
        if "photo" in app_name.lower():
            size_gb *= 1.2  # 20% larger for photo apps
        return super().install_app(app_name, size_gb)

# Demonstration of polymorphism
def smartphone_demo():
    devices = [
        GamingPhone("ROG", "Phone 7", "Android 14", 512, 85, 
                   "Adreno 740", "Vapor Chamber"),
        CameraPhone("Xiaomi", "14 Ultra", "HyperOS", 256, 90,
                   200, "10x Optical")
    ]
    
    for phone in devices:
        print(f"\n=== Using {phone} ===")
        print(phone.toggle_screen())
        print(phone.install_app("Mobile Legends", 5))
        print(phone.install_app("Photo Editor Pro", 2))
        print(phone.perform_task())
        print(phone.check_storage())
        print(f"Battery: {phone.battery_level}%")

if __name__ == "__main__":
    smartphone_demo()