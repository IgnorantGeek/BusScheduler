public class Test
{
    public static void main(String[] args)
    {
        NextBus n = new NextBus();
        n.add_agency_by_tag("cyide");
        n.agencies.get(0).print_routes();
    }
}