from enum import Enum 

class OperatingSystem(Enum):
    WINDOWS = "WINDOWS"
    OSX = "OSX"
    LINUX = "LINUX"

class Package(object):
    def __init__(self, name, version) -> None:
        self.__name = name
        self.__version = version

    def getKey(self):
        return self.__name+self.__version

    def getName(self):
        return self.__name



class DownloadHelper(object):
    def __init__(self, operatingSystem: OperatingSystem) ->None:
        self._cache = {}
        self.operatingSystem = operatingSystem

    def download(self, target: str):
        pass

class PackageRepository(object):

    def __init__(self, operatingSystem: OperatingSystem) -> None:
        self.__downloadMapping = {}
        self.__downloadMapping[OperatingSystem.WINDOWS] = WindowsDownloadHelper()
        self.__createPackageRepository(operatingSystem)
        pass

    def __createPackageRepository(self, operatingSystem: OperatingSystem) -> None:
        self.__mapping = {}
        self.downloadHelper = self.__downloadMapping[operatingSystem]
        return self
    
    def __isPresent(self, package: Package):
        return package.getKey() in self.__mapping

    def getPackageBinaries(self, package: Package):
        print("Getting package binaries for package: ", package.getKey())
        if self.__isPresent(package):
            print("Package is already installed, returning")
            return None
        binaries = self.downloadHelper.download(package.getName())
        self.__mapping[package.getKey()] = binaries
        return binaries

class WindowsDownloadHelper(DownloadHelper):

    def __init__(self) -> None:
        super().__init__(OperatingSystem.WINDOWS)

    def download(self, target: str):
        if target is None:
            return None
        if target in self._cache:
            print("Downloading from cache in Windows")
            return self.cache[target]
        else:
            print("Downloading package :", target, " in Windows ")
            print("updating cache :", target, " in Windows")
            self._cache[target] = "BINARY1234"
            return self._cache[target]

class Installer(object):
    def __init__(self, operatingSystem: OperatingSystem) -> None:
        self.__createInstaller(operatingSystem=operatingSystem)
        pass

    def __createInstaller(self, operatingSystem: OperatingSystem) ->None:
        self.__alreadyInstalledCache = {}
        self.__repository = PackageRepository(operatingSystem)
        
    def getOperatingSystem(self):
        return self.operatingSystem

    def install(self, package: Package):
        if package is None:
            return
        if package.getKey() in self.__alreadyInstalledCache:
            print("Package is already installed")
            return
        self.__repository.getPackageBinaries(package)
        self.__alreadyInstalledCache[package.getKey()] = True



class PackageInstallerSimulator(object):

    def main():

        print("\n\n\nSimulating package installer")
        
        # initialize 
        
        installer = Installer(OperatingSystem.WINDOWS)

        package = Package("Lombok", "1.0.1")
        
        # install
        installer.install(package)

        # downloading again 
        installer.install(package)

    if __name__ == "__main__":
        main()
