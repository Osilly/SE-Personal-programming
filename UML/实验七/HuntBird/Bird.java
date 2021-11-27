public abstract class Bird {
    public FlyBehavior flyBehavior;
    public SwimBehavior swimBehavior;

    public Bird(FlyBehavior flyBehavior, SwimBehavior swimBehavior) {
        this.swimBehavior = swimBehavior;
        this.flyBehavior = flyBehavior;
    }

    public void display() {
        flyBehavior.fly();
        swimBehavior.swim();
    }
}
