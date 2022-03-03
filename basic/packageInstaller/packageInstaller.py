from enum import Enum 

class OperatingSystem(Enum):
    WINDOWS = "WINDOWS"
    OSX = "OSX"
    LINUX = "LINUX"

class Package(object):
    def __init__(self, name, version) -> None:
        self.name = name
        self.version = version

    def getKey(self):
        return self.name+self.version

class DownloadHelper(object):
    def __init__(self, operatingSystem: OperatingSystem) ->None:
        self.cache = {}
        self.operatingSystem = operatingSystem

    def download(self, target: str):
        pass

class PackageRepository(object):

    def __init__(self, downloadHelper: DownloadHelper) -> None:
        self.mapping = {}
        self.downloadHelper = downloadHelper
    
    def __isPresent__(self, package: Package):
        return package.getKey() in self.mapping

    def getPackageBinaries(self, package: Package):
        print("Getting package binaries for package: ", package)
        if self.__isPresent__(package):
            print("Package is already installed, returning")
            return None
        binaries = self.downloadHelper.download(package.name)
        self.mapping[package.getKey()] = binaries
        return binaries

class WindowsDownloadHelper(DownloadHelper):

    def __init__(self) -> None:
        super().__init__(OperatingSystem.WINDOWS)

    def download(self, target: str):
        if target is None:
            return None
        if target in self.cache:
            print("Downloading from cache in Windows")
            return self.cache[target]
        else:
            print("Downloading package :", target, " in Windows ")
            print("updating cache :", target, " in Windows")
            self.cache[target] = "BINARY1234"
            return self.cache[target]

class Installer(object):
    def __init__(self, repository: PackageRepository, operatingSystem: OperatingSystem) ->None:
        self.alreadyInstalledCache = {}
        self.operatingSystem = operatingSystem
        self.repository = repository
        
    def getOperatingSystem(self):
        return self.operatingSystem

    def install(self, package):
        pass

class WindowsInstaller(Installer):

    def __init__(self, repository: PackageRepository) -> None:
        super().__init__(repository, OperatingSystem.WINDOWS)

    def install(self, package: Package):
        if package is None:
            return
        if package.getKey() in self.alreadyInstalledCache:
            print("Package is already installed")
            return 

        self.repository.getPackageBinaries(package)


class PackageInstallerSimulator(object):

    def main():

        print("Simulating package installer")
        
        # initialize 
        
        installer = WindowsInstaller(PackageRepository(WindowsDownloadHelper()))
        package = Package("Lombok", "1.0.1")
        
        # install
        installer.install(package)

        # downloading again 
        installer.install(package)

    if __name__ == "__main__":
        main()
