import {
  SignInButton,
  SignOutButton,
  SignUpButton,
  SignedIn,
  SignedOut,
} from "@clerk/nextjs";
import { Button } from "@/components/ui/button";
import Link from "next/link";

const Navigation = () => {
  return (
    <nav className="border-b border-[var(--foreground)]/10">
      <div className="flex container h-16 items-center justify-between px-4  mx-auto">
        <div className="text-xl font-semibold"><Link href="/">RAG BOT</Link></div>

        <div className="flex gap-2">
          <SignedOut>
            <SignInButton mode="modal">
              <Button variant="ghost">Sign In</Button>
            </SignInButton>
            <SignUpButton mode="modal">
              <Button>Sign Up</Button>
            </SignUpButton>
          </SignedOut>

          <SignedIn>
            <Button variant="link">
              <Link href="/upload">Upload</Link>
            </Button>
            <Button variant="link">
              <Link href="/chat">Chat</Link>
            </Button>
            <SignOutButton>
              <Button variant="outline">Sign Out</Button>
            </SignOutButton>
          </SignedIn>
        </div>
      </div>
    </nav>
  );
};
export default Navigation;
