import clsx from "clsx"
import { useCollections } from "medusa-react"
import Link from "next/link"
import CountrySelect from "../country-select"

const FooterNav = () => {
  const { collections } = useCollections()

  return (
    <div
      id="footer"
      className="content-container flex flex-col gap-y-8 pt-16 pb-8"
    >
      <div className="flex flex-col gap-y-6 xsmall:flex-row items-start justify-between">
        <Link href="/">
          <a className="text-xl-semi uppercase">Primes as a Service</a>
        </Link>
      </div>
      <div>
        <CountrySelect />
      </div>
      <div className="flex flex-col-reverse gap-y-4 justify-center xsmall:items-center xsmall:flex-row xsmall:items-end xsmall:justify-between">
        <span className="text-small-regular text-white-500">
          Copyright 2022 © Primes as a Service
        </span>
      </div>
    </div>
  )
}

export default FooterNav
