package explore;

import java.util.*;
import java.time.Instant;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;
import java.util.UUID;
import java.util.stream.Collectors;
import java.util.Optional;
import java.util.function.BinaryOperator;
import java.util.function.Function;

public class FilterExperiment2 {

    public void split(EnhancedVehicleRunContext enhancedVehicleRunContext) {
        VehicleRun vehicleRun = enhancedVehicleRunContext.getEntity();
        Map<RunStructureIdentifier, RunStructure> runStructures = enhancedVehicleRunContext.getRunStructures();

        List<Signal> signals = findAllLatestSignalsByEntityId(vehicleRun.getVehicleRunIdentifier());

        // we can have multiple signals at a particular stop
        Map<String, Signal> signalMap = signals.stream()
                                                .collect(Collectors.toMap(Signal::getSignalId, Function.identity()));
        
        vehicleRun
            .getVehicleStops()
            .stream()
            .map(stop -> signals.stream().filter(signal -> signal.get)


        // Optional<Signal> maybeSignal = signalService.findByEntityId(vehicleRun.getVehicleRunIdentifier());
        // // Signal stop1 should match
        // // all signal types should be allowed
        // // need to add a for each on each signal returned from signal service
        // return vehicleRun.getVehicleStops().stream()
        //     .map(s -> maybeSignal.map(Signal::getSignalContext)
        //         .filter(signal -> signal instanceof VehicleStopSignalContext)
        //         .map(signalContext -> (VehicleStopSignalContext) signalContext)
        //         .filter(signalContext -> signalContext.getStopId().equals(s.getStopId()))
        //         .map(signal -> new EnhancedVehicleStopContext(vehicleRun, runStructures, s.getStopId(),
        //             VersionedSignalIdentifier.builder()
        //                 .id(maybeSignal.get().getSignalId())
        //                 .version(maybeSignal.get().getSignalVersion())
        //                 .build()))
        //         .orElseGet(() -> new EnhancedVehicleStopContext(vehicleRun, runStructures, s.getStopId())))
        //     .collect(Collectors.toSet());
    }
    

    public static List<Signal> findAllLatestSignalsByEntityId(String entityId) {
        List<Signal> latestSignals = findAllSignalsByEntityId(entityId);
        print(latestSignals);
        System.out.println("Size: "+latestSignals.size());
        List<Signal> temp = latestSignals
        .stream()
        .filter(signal -> isTerminalSignalStatus(signal.getStatus()))
        .collect(Collectors.toList());

        System.out.println("Size: "+temp.size());
        // Collection<User> latestVersions = users.stream()
        //     .collect(Collectors.groupingBy(User::getUserId,
        //             Collectors.collectingAndThen(Collectors.maxBy(Comparator.comparing(User::getVersionNumber)), Optional::get)))
        //             .values();


        latestSignals = new ArrayList<> (latestSignals
                .stream()
                .filter(signal -> isTerminalSignalStatus(signal.getStatus()))
                .filter(signal -> signal.getLastModifiedDate().isAfter(Instant.now().minusSeconds(ACTIONABLE_SIGNALS_TIME_THRESHOLD)))
                .collect(Collectors.toMap(Signal::getSignalId, Function.identity(), BinaryOperator.maxBy(Comparator.comparing(Signal::getSignalVersion)))).values());
        Collection<Signal> latestVersion = latestSignals
        .stream()
        .collect(Collectors.groupingBy(Signal::getSignalId, Collectors.collectingAndThen(Collectors.maxBy(Comparator.comparing(Signal::getSignalVersion)), Optional::get))).values();
        
        print(new LinkedList<>(latestVersion));
        System.out.println("====");
        return latestSignals;

    }

    private static void print(List<Signal> result) {
        System.out.println("Printing list");
        for (Signal signal: result) {
            System.out.println(signal.signalId+" "+signal.version+" "+signal.getStatus()+" "+signal.getLastModifiedDate());
        }
    }

    private static boolean isTerminalSignalStatus(String target) {
        return target.equals("INACTIVE") ? false: true;
    }

    private static List<Signal> findAllSignalsByEntityId(String target) {
        List<Signal> response = new ArrayList<>();
        response.add(getSignal("ACTIVE", "NO_EMPTIES_SIGNAL", Instant.now(), 1));
        response.add(getSignal("INACTIVE","NO_EMPTIES_SIGNAL", Instant.now(), 2));
        response.add(getSignal("ACTIVE", "NO_EMPTIES_SIGNAL", Instant.now().minusSeconds(1000), 1));
        response.add(getSignal("ACTIVE", "CARGO_NOT_DELIVERED", Instant.now(), 1));
        Signal signal = response.get(0).copy();
        signal.version = 2;
        signal.lastModifiedDate = Instant.now();
        response.add(signal);
        return response;
    }

    private static Signal getSignal(String status, String type, Instant modifiedDate, int version) {
        Signal signal = new Signal();
        signal.signalId = UUID.randomUUID().toString();
        signal.signalStatus = status;
        signal.lastModifiedDate = modifiedDate;
        signal.version = version;
        return signal;
    }
    

    public static void main(String ar[]) {

    }
    
}


class Signal {
    String signalId;
    int version;
    String signalStatus;
    String type;
    Instant lastModifiedDate;
    VehicleStop stopId;

    // where is stop id stored in signals ?
    public VehicleStop getStopId() {
        return stopId;
    }

    public String getSignalId() {
        return signalId;
    }

    public int getSignalVersion() {
        return version;
    }

    public String getStatus() {
        return signalStatus;
    }

    public Instant getLastModifiedDate() {
        return lastModifiedDate;
    }

    public Signal copy() {
        Signal signal = this;
        Signal response = new Signal();
        response.lastModifiedDate = signal.lastModifiedDate;
        response.signalId = signal.signalId;
        response.signalStatus = signal.signalStatus;
        response.type = signal.type;
        response.version = signal.version;
        return response;
    }

}


class EnhancedVehicleStopContext {

}

class VehicleStop {


}
class VehicleRun {
    List<VehicleStop> vehicleStops;
    String id;

    public List<VehicleStop> getVehicleStops() {
        return vehicleStops;
    }

    public String getVehicleRunIdentifier() {
        return id;
    }
}
class RunStructureIdentifier {

}

class RunStructure {

}

class EnhancedVehicleRunContext {
    VehicleRun vehicleRun;
    Map<RunStructureIdentifier, RunStructure> runStructures;

    public VehicleRun getEntity() {
        return vehicleRun;
    }

    public Map<RunStructureIdentifier, RunStructure> getRunStructures() {
        return runStructures;
    }
}
