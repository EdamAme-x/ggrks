import { PageProps } from "$fresh/server.ts";

export default function Greet(props: PageProps) {
  return <script>{"location.href = 'https://google.com/search?q=" + props.params.query + "'"} </script>;
}
