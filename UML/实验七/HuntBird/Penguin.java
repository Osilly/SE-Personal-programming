public class Penguin extends Bird {
    public Penguin(FlyBehavior flyBehavior, SwimBehavior swimBehavior) {
        super(flyBehavior, swimBehavior);
    }

    public void display() {
        System.out.println("企鹅");
        super.display();
    }
}
