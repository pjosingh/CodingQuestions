package explore;

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


class FilterExperiment {

    private final static int ACTIONABLE_SIGNALS_TIME_THRESHOLD = 900;

    public static List<Signal1> findAllLatestSignalsByEntityId(String entityId) {
        List<Signal1> latestSignals = findAllSignalsByEntityId(entityId);
        print(latestSignals);
        System.out.println("Size: "+latestSignals.size());
        List<Signal1> temp = latestSignals
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
                .collect(Collectors.toMap(Signal1::getSignalId, Function.identity(), BinaryOperator.maxBy(Comparator.comparing(Signal1::getSignalVersion)))).values());
        Collection<Signal1> latestVersion = latestSignals
        .stream()
        .collect(Collectors.groupingBy(Signal1::getSignalId, Collectors.collectingAndThen(Collectors.maxBy(Comparator.comparing(Signal1::getSignalVersion)), Optional::get))).values();
        
        print(new LinkedList<>(latestVersion));
        System.out.println("====");
        return latestSignals;

    }

    private static boolean isTerminalSignalStatus(String target) {
        return target.equals("INACTIVE") ? false: true;
    }

    private static List<Signal1> findAllSignalsByEntityId(String target) {
        List<Signal1> response = new ArrayList<>();
        response.add(getSignal("ACTIVE", "NO_EMPTIES_SIGNAL", Instant.now(), 1));
        response.add(getSignal("INACTIVE","NO_EMPTIES_SIGNAL", Instant.now(), 2));
        response.add(getSignal("ACTIVE", "NO_EMPTIES_SIGNAL", Instant.now().minusSeconds(1000), 1));
        response.add(getSignal("ACTIVE", "CARGO_NOT_DELIVERED", Instant.now(), 1));
        Signal1 signal = response.get(0).copy();
        signal.version = 2;
        signal.lastModifiedDate = Instant.now();
        response.add(signal);
        return response;
    }

    private static Signal1 getSignal(String status, String type, Instant modifiedDate, int version) {
        Signal1 signal = new Signal1();
        signal.signalId = UUID.randomUUID().toString();
        signal.signalStatus = status;
        signal.lastModifiedDate = modifiedDate;
        signal.version = version;
        return signal;
    }

    private static void print(List<Signal1> result) {
        System.out.println("Printing list");
        for (Signal1 signal: result) {
            System.out.println(signal.signalId+" "+signal.version+" "+signal.getStatus()+" "+signal.getLastModifiedDate());
        }
    }


    public static void main(String ar[]) {
        System.out.println("Hello world ");
        List<Signal1> result = findAllLatestSignalsByEntityId(new String("VR1"));
        print(result);
    }
}

class Signal1 {
    String signalId;
    int version;
    String signalStatus;
    String type;
    Instant lastModifiedDate;

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

    public Signal1 copy() {
        Signal1 signal = this;
        Signal1 response = new Signal1();
        response.lastModifiedDate = signal.lastModifiedDate;
        response.signalId = signal.signalId;
        response.signalStatus = signal.signalStatus;
        response.type = signal.type;
        response.version = signal.version;
        return response;
    }

}