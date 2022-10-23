import UnderlineLink from "@modules/common/components/underline-link"
import Image from "next/image"

const FooterCTA = () => {
  return (
    <div id="shopping" className="bg-blue-100 w-full">
      <div className="content-container flex flex-col-reverse gap-y-8 small:flex-row small:items-center justify-between py-16 relative">
        <div>
          <h3 id="shop-latest" className="text-2xl-semi">
            Shop the latest primes
          </h3>
          <div id="shop-latest" className="mt-6">
            <UnderlineLink href="/store">Explore products</UnderlineLink>
          </div>
        </div>
      </div>
    </div>
  )
}

export default FooterCTA
