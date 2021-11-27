public class Client {

    public static void main(String[] args) {
        Bird eagle = new Eagle(new FreeFly(), new UnableSwim());
        eagle.display();
        Bird penguin = new Penguin(new UnableFly(), new AbleSwim());
        penguin.display();
    }
}
