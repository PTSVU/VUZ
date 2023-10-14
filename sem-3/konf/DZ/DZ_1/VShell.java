package vuz.konf.dz1;

import java.io.*;
import java.util.*;
import java.nio.file.*;
import java.io.File;
import java.io.IOException;
import java.util.zip.ZipEntry;
import java.util.zip.ZipInputStream;
import java.util.zip.ZipOutputStream;


public class VShell {
    public String currentDirectory;
    private final Stack<String> directoryHistory;
    private final Scanner scanner;
    private final Map<String, String> environmentVariables;
    public static String zipFileName = "VShellRoot.zip";
    public static String sourceFolderPath = "VShellRoot";

    public VShell() {
        scanner = new Scanner(System.in);
        environmentVariables = new HashMap<>();
        currentDirectory = ".\\VShellRoot";
        directoryHistory = new Stack<>();

        File rootDir = new File(currentDirectory);
        if (!rootDir.exists()) {
            rootDir.mkdir();
        }

        File zipFile = new File("VShellRoot.zip");
        if (!zipFile.exists()) {
            createInitialZipArchive(zipFile);
        }
    }

    private void createInitialZipArchive(File zipFile) {
        try {
            FileOutputStream fos = new FileOutputStream(zipFile);
            ZipOutputStream zos = new ZipOutputStream(fos);
            zos.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void run() {
        while (true) {
            zipAct();
            System.out.print(currentDirectory + " $ ");
            String command = scanner.nextLine().trim();

            if (command.startsWith("--script")) {
                String scriptFileName = command.replace("--script", "").trim();
                executeScript(scriptFileName);
                continue;
            }

            String[] commandParts = command.split(" ");
            String cmd = commandParts[0];
            switch (cmd) {
                case "pwd" -> printCurrentDirectory();
                case "ls" -> {
                    if (commandParts.length == 1) {
                        listFiles();
                    } else if (commandParts.length == 2) {
                        String directoryName = commandParts[1];
                        listDeeper(directoryName);
                    } else {
                        System.out.println("Error");
                    }
                }
                case "cd" -> {
                    if (commandParts.length > 1 && !commandParts[1].equals("")) {
                        changeDirectory(commandParts[1]);
                    } else {
                        System.out.println("Use 'cd <directory>' to change the directory.");
                    }
                }
                case "cat" -> {
                    if (commandParts.length > 1) {
                        readFile(commandParts[1]);
                    } else {
                        System.out.println("Use 'cat <file>' to view the contents of a file.");
                    }
                }
                case "mkdir" -> {
                    if (commandParts.length > 1) {
                        mkdir(commandParts[1]);
                    } else {
                        System.out.println("Use 'mkdir <directory>' to create a directory.");
                    }
                }
                case "rmdir" -> {
                    if (commandParts.length > 1) {
                        rmdir(commandParts[1]);
                    } else {
                        System.out.println("Use 'rmdir <directory>' to remove a directory.");
                    }
                }
                case "rm" -> {
                    if (commandParts.length > 1) {
                        rm(commandParts[1]);
                    } else {
                        System.out.println("Use 'rm <file>' to remove a file.");
                    }
                }
                case "touch" -> {
                    if (commandParts.length > 1) {
                        touch(commandParts[1]);
                    } else {
                        System.out.println("Use 'touch <file>' to create a new file.");
                    }
                }
                case "mv"  -> {
                    if (commandParts.length > 2) {
                        mv(commandParts[1], commandParts[2]);
                    } else {
                        System.out.println("Use 'mv <source> <destination>' to move a file or directory.");
                    }
                }
                case "echo" -> {
                    if (commandParts.length > 1) {
                        StringBuilder echoText = new StringBuilder();
                        for (int i = 1; i < commandParts.length; i++) {
                            echoText.append(commandParts[i]).append(" ");
                        }
                        echo(echoText.toString().trim());
                    } else {
                        System.out.println("Use 'echo <text>' to display text.");
                    }
                }
                case "grep" -> {
                    if (commandParts.length > 2) {
                        grep(commandParts[1], commandParts[2]);
                    } else {
                        System.out.println("Use 'grep <pattern> <file>' to search for a pattern in a file.");
                    }
                }
                case "find" -> {
                    if (commandParts.length > 1) {
                        String fileNameToFind = commandParts[1];
                        find(currentDirectory, fileNameToFind);
                    } else {
                        System.out.println("Use 'find <file_name>' to search for files.");
                    }
                }
                case "set" -> {
                    if (commandParts.length > 2) {
                        setEnvironmentVariable(commandParts[1], commandParts[2]);
                    } else {
                        System.out.println("Use 'set <variable> <value>' to set an environment variable.");
                    }
                }
                case "get" -> {
                    if (commandParts.length > 1) {
                        getEnvironmentVariable(commandParts[1]);
                    } else {
                        System.out.println("Use 'get <variable>' to get the value of an environment variable.");
                    }
                }
                case "exit" -> System.exit(0);
                case "help" -> help();
                default -> System.out.println("Unknown command: " + cmd);
            }
            zipAct();
        }
    }


    private void printCurrentDirectory() {
        System.out.println(currentDirectory);
    }

    private void listFiles() {
        File dir = new File(currentDirectory);
        File[] files = dir.listFiles();
        if (files != null) {
            for (File file : files) {
                System.out.println("\t" + file.getName());
            }
        }
    }

    private void listDeeper(String directoryName) {
        boolean lD = false;
        File dir = new File(currentDirectory);
        File[] files = dir.listFiles();
        if (files != null) {
            for (File file : files) {
                if (directoryName.equals(file.getName())) {
                    lD = true;
                    byName(directoryName);
                    File dirr = new File(currentDirectory);
                    File[] filess = dirr.listFiles();
                    if (filess != null) {
                        for (File filee : filess) {
                            System.out.println("\t" + filee.getName());
                        }
                    }
                    byName("..");
                }
            }
        }
        if (!lD) {
            System.out.println("Directory not found");
        }
    }

    private void byName(String directoryName) {
        if (directoryName.equals("..")) {
            if (!directoryHistory.isEmpty()) {
                currentDirectory = directoryHistory.pop();
            }
        } else {
            directoryHistory.push(currentDirectory);
            File newDir = new File(currentDirectory, directoryName);
            if (newDir.isDirectory()) {
                currentDirectory = currentDirectory + "\\" + directoryName;
            }
        }
    }

    private void changeDirectory(String directoryName) {
        if (directoryName.equals("..")) {
            if (!directoryHistory.isEmpty()) {
                currentDirectory = directoryHistory.pop();
                System.out.println("Changed directory to: " + currentDirectory);
            } else {
                System.out.println("No previous directory to return to.");
            }
        } else {
            boolean containsOnlyValidCharacters = directoryName.matches("[./\\\\]+");
            if (!containsOnlyValidCharacters) {
                directoryHistory.push(currentDirectory);
                File newDir = new File(currentDirectory, directoryName);
                if (newDir.exists()) {
                    currentDirectory = currentDirectory + "\\" + directoryName;
                    System.out.println("Changed directory to: " + currentDirectory);
                } else {
                    System.out.println("Directory not found: " + directoryName);
                }
            } else {
                System.out.println(directoryName + " is not directory");
            }
        }
    }

    private void readFile(String fileName) {
        try {
            String filePath = currentDirectory + File.separator + fileName;
            List<String> lines = Files.readAllLines(Paths.get(filePath));
            for (String line : lines) {
                System.out.println(line);
            }
        } catch (IOException e) {
            System.out.println("Error when reading a file: " + e.getMessage());
        }
    }

    private void mkdir(String directoryName) {
        File newDir = new File(currentDirectory, directoryName);

        if (!newDir.exists()) {
            if (newDir.mkdir()) {
                System.out.println("Created directory: " + currentDirectory + "\\" + newDir.getName());
            } else {
                System.out.println("Failed to create directory: " + currentDirectory + "\\" + newDir.getName());
            }
        } else {
            System.out.println("Directory already exists: " + currentDirectory + "\\" + newDir.getName());
        }
    }

    private void rmdir(String directoryName) {
        File dirToDelete = new File(currentDirectory, directoryName);

        if (dirToDelete.exists() && dirToDelete.isDirectory()) {
            if (dirToDelete.list().length == 0) {
                if (dirToDelete.delete()) {
                    System.out.println("Deleted directory: " + currentDirectory + "\\" + dirToDelete.getName());
                } else {
                    System.out.println("Failed to delete directory: " + currentDirectory + "\\" + dirToDelete.getName());
                }
            } else {
                System.out.println("Directory is not empty: " + currentDirectory + "\\" + dirToDelete.getName());
            }
        } else {
            System.out.println("Directory not found: " + currentDirectory + "\\" + dirToDelete.getName());
        }
    }

    private void rm(String fileName) {
        File fileToDelete = new File(currentDirectory, fileName);

        if (fileToDelete.exists() && fileToDelete.isFile()) {
            if (fileToDelete.delete()) {
                System.out.println("Deleted file: " + currentDirectory + "\\" + fileToDelete.getName());
            } else {
                System.out.println("Failed to delete file: " + currentDirectory + "\\" + fileToDelete.getName());
            }
        } else {
            System.out.println("File not found: " + currentDirectory + "\\" + fileToDelete.getName());
        }
    }

    private void touch(String fileName) {
        File newFile = new File(currentDirectory, fileName);

        try {
            if (newFile.createNewFile()) {
                System.out.println("Created file: " + currentDirectory + "\\" + newFile.getName());
            } else {
                System.out.println("File already exists: " + currentDirectory + "\\" + newFile.getName());
            }
        } catch (IOException e) {
            System.out.println("Failed to create file: " + currentDirectory + "\\" + newFile.getName());
        }
    }

    private void mv(String source, String destination) {
        File sourceFile = new File(currentDirectory, source);
        File destFile = new File(destination);

        if (sourceFile.exists()) {
            if (sourceFile.renameTo(destFile)) {
                System.out.println("Moved " + currentDirectory + "\\" + sourceFile.getName() + " to " + currentDirectory + "\\" + destFile.getName());
            } else {
                System.out.println("Failed to move " + currentDirectory + "\\" + sourceFile.getName());
            }
        } else {
            System.out.println("File or directory not found: " + currentDirectory + "\\" + sourceFile.getName());
        }
    }
    private void echo(String text) {
        System.out.println(text);
    }

    private void grep(String pattern, String fileName) {
        try {
            String filePath = currentDirectory + File.separator + fileName;
            List<String> lines = Files.readAllLines(Paths.get(filePath));
            for (String line : lines) {
                if (line.contains(pattern)) {
                    System.out.println(line);
                }
            }
        } catch (IOException e) {
            System.out.println("Error when reading the file: " + e.getMessage());
        }
    }

    private void find(String directoryPath, String fileName) {
        File directory = new File(directoryPath);
        File[] files = directory.listFiles();

        if (files != null) {
            for (File file : files) {
                if (file.isDirectory()) {
                    find(file.getAbsolutePath(), fileName);
                } else if (file.getName().equals(fileName)) {
                    System.out.println(file.getAbsolutePath());
                }
            }
        }
    }


    private void setEnvironmentVariable(String name, String value) {
        environmentVariables.put(name, value);
    }

    private void getEnvironmentVariable(String name) {
        String value = environmentVariables.get(name);
        if (value != null) {
            System.out.println(name + " = " + value);
        } else {
            System.out.println("Environment variable not found: " + name);
        }
    }

    private void executeScript(String scriptFileName) {
        try (BufferedReader reader = new BufferedReader(new FileReader(scriptFileName))) {
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println("Script execution: " + line);
                executeCommand(line);
            }
        } catch (IOException e) {
            System.out.println("Error during script execution: " + e.getMessage());
        }
    }

    public String executeCommand(String command) {
        String[] commandParts = command.split(" ");
        String cmd = commandParts[0];

        switch (cmd) {
            case "pwd" -> printCurrentDirectory();
                case "ls" -> {
                    if (commandParts.length == 1) {
                        listFiles();
                    } else if (commandParts.length == 2) {
                        String directoryName = commandParts[1];
                        listDeeper(directoryName);
                    } else {
                        System.out.println("Error");
                    }
                }
                case "cd" -> {
                    if (commandParts.length > 1) {
                        changeDirectory(commandParts[1]);
                    } else {
                        System.out.println("Use 'cd <directory>' to change the directory.");
                    }
                }
                case "cat" -> {
                    if (commandParts.length > 1) {
                        readFile(commandParts[1]);
                    } else {
                        System.out.println("Use 'cat <file>' to view the contents of a file.");
                    }
                }
                case "mkdir" -> {
                    if (commandParts.length > 1) {
                        mkdir(commandParts[1]);
                    } else {
                        System.out.println("Use 'mkdir <directory>' to create a directory.");
                    }
                }
                case "rmdir" -> {
                    if (commandParts.length > 1) {
                        rmdir(commandParts[1]);
                    } else {
                        System.out.println("Use 'rmdir <directory>' to remove a directory.");
                    }
                }
                case "rm" -> {
                    if (commandParts.length > 1) {
                        rm(commandParts[1]);
                    } else {
                        System.out.println("Use 'rm <file>' to remove a file.");
                    }
                }
                case "touch" -> {
                    if (commandParts.length > 1) {
                        touch(commandParts[1]);
                    } else {
                        System.out.println("Use 'touch <file>' to create a new file.");
                    }
                }
                case "mv"  -> {
                    if (commandParts.length > 2) {
                        mv(commandParts[1], commandParts[2]);
                    } else {
                        System.out.println("Use 'mv <source> <destination>' to move a file or directory.");
                    }
                }
                case "echo" -> {
                    if (commandParts.length > 1) {
                        StringBuilder echoText = new StringBuilder();
                        for (int i = 1; i < commandParts.length; i++) {
                            echoText.append(commandParts[i]).append(" ");
                        }
                        echo(echoText.toString().trim());
                    } else {
                        System.out.println("Use 'echo <text>' to display text.");
                    }
                }
                case "grep" -> {
                    if (commandParts.length > 2) {
                        grep(commandParts[1], commandParts[2]);
                    } else {
                        System.out.println("Use 'grep <pattern> <file>' to search for a pattern in a file.");
                    }
                }
                case "find" -> {
                    if (commandParts.length > 1) {
                        String fileNameToFind = commandParts[1];
                        find(currentDirectory, fileNameToFind);
                    } else {
                        System.out.println("Use 'find <file_name>' to search for files.");
                    }
                }
                case "set" -> {
                    if (commandParts.length > 2) {
                        setEnvironmentVariable(commandParts[1], commandParts[2]);
                    } else {
                        System.out.println("Use 'set <variable> <value>' to set an environment variable.");
                    }
                }
                case "get" -> {
                    if (commandParts.length > 1) {
                        getEnvironmentVariable(commandParts[1]);
                    } else {
                        System.out.println("Use 'get <variable>' to get the value of an environment variable.");
                    }
                }
                case "exit" -> System.exit(0);
                case "help" -> help();
                default -> System.out.println("Unknown command: " + cmd);
        }
        return cmd;
    }

    private void help() {
    System.out.println("""
            Available commands:
            \tpwd - Print current directory.
            \tls - List files and directories in the current directory.
            \tcd <directory> - Change the current directory.
            \tcat <file> - View the contents of a file.
            \tset <variable> <value> - Set an environment variable.
            \tget <variable> - Get the value of an environment variable.
            \techo <text> - Write text to a file.
            \tfind <file_name> - Search for files with the given name in all subdirectories.
            \tmkdir <directory> - Create a new directory.
            \trmdir <directory> - Remove a directory.
            \trm <file> - Remove a file.
            \ttouch <file> - Create a new empty file.
            \tmv <source> <destination> - Move or rename a file/directory.
            \tgrep <pattern> <file> - Search for a pattern in a file.
            \thelp - Display this help message.
            \texit - Exit the VShell.
            """);
    }

    public static void clearZipArchive(String zipFileName) throws IOException {
        try (FileOutputStream fos = new FileOutputStream(zipFileName);
             ZipOutputStream zos = new ZipOutputStream(fos)) {
        }
    }

public static void copyFolderToZip(String sourceFolderPath, String zipFileName) throws IOException {
        try (FileOutputStream fos = new FileOutputStream(zipFileName);
             ZipOutputStream zos = new ZipOutputStream(fos)) {
            File sourceFolder = new File(sourceFolderPath);
            addToZip(sourceFolder, sourceFolder, zos);
        }
    }

    private static void addToZip(File rootFolder, File fileOrFolder, ZipOutputStream zos) throws IOException {
        if (fileOrFolder.isDirectory()) {
            File[] files = fileOrFolder.listFiles();
            if (files != null) {
                for (File file : files) {
                    addToZip(rootFolder, file, zos);
                }
            }
        } else {
            String entryName = fileOrFolder.getPath().substring(rootFolder.getPath().length() + 1);
            try (FileInputStream fis = new FileInputStream(fileOrFolder)) {
                ZipEntry zipEntry = new ZipEntry(entryName);
                zos.putNextEntry(zipEntry);

                byte[] buffer = new byte[1024];
                int bytesRead;
                while ((bytesRead = fis.read(buffer)) != -1) {
                    zos.write(buffer, 0, bytesRead);
                }

                zos.closeEntry();
            }
        }
    }

    public static void extractZipArchive(String zipFileName, String destinationFolder) throws IOException {
        File destDir = new File(destinationFolder);
        if (!destDir.exists()) {
            destDir.mkdirs();
        }

        try (ZipInputStream zipInputStream = new ZipInputStream(new FileInputStream(zipFileName))) {
            ZipEntry entry;
            while ((entry = zipInputStream.getNextEntry()) != null) {
                if (!entry.isDirectory()) {
                    String entryName = entry.getName();
                    File entryFile = new File(destinationFolder, entryName);

                    File entryDir = entryFile.getParentFile();
                    if (!entryDir.exists()) {
                        entryDir.mkdirs();
                    }

                    try (FileOutputStream fos = new FileOutputStream(entryFile)) {
                        byte[] buffer = new byte[1024];
                        int length;
                        while ((length = zipInputStream.read(buffer)) > 0) {
                            fos.write(buffer, 0, length);
                        }
                    }
                }
            }
        }
    }

    public static void zipAct() {
        try {
            clearZipArchive(zipFileName);
            copyFolderToZip(sourceFolderPath, zipFileName);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

//    public static void deleteFolder(File folder) {
//        if (folder.exists()) {
//            File[] files = folder.listFiles();
//            if (files != null) {
//                for (File file : files) {
//                    if (file.isDirectory()) {
//                        deleteFolder(file);
//                    }
//                }
//            }
//        }
//    }
//
//    public static void deleteVShellRootFolder() {
//        File vShellRoot = new File(sourceFolderPath);
//        deleteFolder(vShellRoot);
//    }

    public static void main(String[] args) {
        try {
            extractZipArchive(zipFileName, sourceFolderPath);
        } catch (IOException e) {
            e.printStackTrace();
        }
        VShell vshell = new VShell();
        vshell.run();
        zipAct();
//        deleteVShellRootFolder();
    }
}